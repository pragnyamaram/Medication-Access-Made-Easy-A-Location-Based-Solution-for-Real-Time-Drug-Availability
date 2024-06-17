document.getElementById('medicine-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const medicine = document.getElementById('medicine').value;

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            fetch(`/search?medicine=${medicine}&lat=${latitude}&lng=${longitude}`)
                .then(response => response.json())
                .then(data => {
                    const resultsDiv = document.getElementById('results');
                    resultsDiv.innerHTML = '';
                    if (data.length > 0) {
                        data.forEach(store => {
                            const storeDiv = document.createElement('div');
                            storeDiv.innerHTML = `<strong>${store.name}</strong><br>Address: ${store.address}<br>Distance: ${store.distance} km<br>`;
                            resultsDiv.appendChild(storeDiv);
                        });
                    } else {
                        resultsDiv.innerHTML = 'No stores found with the specified medicine.';
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    document.getElementById('results').innerHTML = 'An error occurred. Please try again.';
                });
        });
    } else {
        alert('Geolocation is not supported by this browser.');
    }
});
