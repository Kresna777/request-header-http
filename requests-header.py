# meng kustom request header dengan package requests
import requests

# url / link web
url = "https://httpbin.org/headers"

# header
header = {
        "User-Agent" : "White Hat"
        }
        

request = requests.get(url, headers=header)

print(request.text)
