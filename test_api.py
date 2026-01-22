import requests

url = "https://jsonplaceholder.typicode.com/post/1"

response = requests.get(url)
print(response.status_code)
print(response.json())
