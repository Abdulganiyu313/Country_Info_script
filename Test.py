import requests

api_key = "358af6bca2c3a9fe7128dda7b6200384"
lat = 6.524379
lon = 3.379206

url = "https://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key
}

response = requests.get(url, params=params) 
print(response.status_code) # Check if the request was successful (200 OK)
data = response.json()

print(data)

