CREATE TABLE pharmacies (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    medicine TEXT NOT NULL
);

-- Insert sample data
INSERT INTO pharmacies (name, address, latitude, longitude, medicine)
VALUES ('Pharmacy A', '123 Main St', 40.7128, -74.0060, 'Aspirin');
INSERT INTO pharmacies (name, address, latitude, longitude, medicine)
VALUES ('Pharmacy B', '456 Elm St', 40.7128, -74.0060, 'Ibuprofen');
select * from pharmacies;