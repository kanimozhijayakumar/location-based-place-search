import requests
import time

locations = [
    ("Chennai", 13.0827, 80.2707),
    ("Bangalore", 12.9716, 77.5946),
    ("Hyderabad", 17.3850, 78.4867)
]

start = time.time()

for city, lat, lon in locations:
    url = "https://dummyjson.com/users/1"  # Demo API
    response = requests.get(url)
    data = response.json()
    print(f"City: {city}, Lat: {lat}, Lon: {lon}, Place Owner: {data['firstName']}")

end = time.time()
print("Total Time (Serial):", end - start, "seconds")
