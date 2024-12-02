import requests
from pprint import pprint

API_Key = '8f9dd4d114e5475777bada396d08d28c'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city 

weather_data = requests.get(base_url).json()

pprint(weather_data)