import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests
from pprint import pprint


#Provide your IBM Watson Device Credentials
organization = "uaortj"
deviceType = "weatherapptype"
deviceId = "weatherappid"
authMethod = "token"
authToken = "app12345678"

city = input('Enter your city : ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=b23b5fad240356d80f95242dcf1d6cad'.format(city)

res = requests.get(url)

data = res.json()

temp = data['main']['temp']
humidity = data['main']['humidity']

wind_speed = data['wind']['speed']

latitude = data['coord']['lat']
longitude = data['coord']['lon']

visibility = data['visibility']

main = data['weather'][0]['main']
description = data['weather'][0]['description']

print('Temperature : {} degree celcius'.format(temp))
print('Humidity : {} %'.format(humidity))

print('Wind Speed : {} m/s'.format(wind_speed))

print('Latitude : {}'.format(latitude))
print('Longitude : {}'.format(longitude))

print('Visibility : {}'.format(visibility))

print('Main : {}'.format(main))
print('Description : {}'.format(description))
