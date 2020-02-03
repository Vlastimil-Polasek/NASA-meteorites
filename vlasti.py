
import requests

result = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
x = result.json()
print("JSON with all meteorites data:")
print(x)








