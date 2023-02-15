import requests
from pprint import pprint
shahar = input("SHahar kititing")
url = f"https://open-weather13.p.rapidapi.com/city/{shahar}"

headers = {
    "X-RapidAPI-Key": "fcbc9f002emsh198a497f3a391d6p177e38jsn86e86532949a",
    "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)
data = response.json()
joylashuv = data['name']
n_t = (data['main']['temp']-32)*(5/9)//1
min_t = data['main']["temp_min"]
max_t = data['main']["temp_max"]
havo = data['weather'][0]['main']
shamol = data['wind']['speed']//1
if havo == "Rain":
    havo = "Yomg'ir"
elif havo == "Mist":
    havo = "Tuman"

print(response.text)
print(f"Bugun {joylashuv}da {n_t} °C, shamol tezligi {shamol} m/s, havo {havo}")




# °C = (°F - 32) × 5/9