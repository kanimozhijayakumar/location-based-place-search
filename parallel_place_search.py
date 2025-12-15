import asyncio
import aiohttp
import time

locations = [
    ("Chennai", 13.0827, 80.2707),
    ("Bangalore", 12.9716, 77.5946),
    ("Hyderabad", 17.3850, 78.4867)
]

async def fetch(session, city, lat, lon):
    url = "https://dummyjson.com/users/1"
    async with session.get(url) as response:
        data = await response.json()
        print(f"City: {city}, Lat: {lat}, Lon: {lon}, Place Owner: {data['firstName']}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, city, lat, lon) for city, lat, lon in locations]
        await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()

print("Total Time (Parallel):", end - start, "seconds")
