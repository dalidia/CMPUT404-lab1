import requests

print("Version of requests library", requests.__version__)
google_page = requests.get("http://google.com/")
