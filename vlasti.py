
import requests

result = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
x = result.json()
print(x)








