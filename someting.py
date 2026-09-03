import requests

url = 'http://api.open-notify.org/astros.json'

response = requests.get(url)

data = response.json()

print(data)