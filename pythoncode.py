from flask import Flask, request, jsonify
from waitress import serve
import sqlite3
from math import radians, cos, sin, sqrt, atan2

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('pharmacy.db')
    conn.row_factory = sqlite3.Row
    return conn

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

@app.route('/search', methods=['GET'])
def search():
    medicine = request.args.get('medicine')
    lat = float(request.args.get('lat'))
    lng = float(request.args.get('lng'))

    conn = get_db_connection()
    cursor = conn.execute("SELECT name, address, latitude, longitude FROM pharmacies WHERE medicine = ?", (medicine,))
    stores = cursor.fetchall()
    conn.close()

    results = []
    for store in stores:
        distance = haversine(lat, lng, store['latitude'], store['longitude'])
        if distance <= 10:  # Filter stores within 10 km radius
            results.append({
                'name': store['name'],
                'address': store['address'],
                'distance': round(distance, 2)
            })

    return jsonify(results)


if __name__ == '__main__':
    serve(app, host='0.0.0.0',port=50200,threads=4)
