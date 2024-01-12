import requests

Base = ""

response = requests.get(Base + "helloworld")
print(response.json())