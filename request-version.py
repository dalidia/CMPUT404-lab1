import requests

print("Version of requests library", requests.__version__)

google_page = requests.get("http://google.com/")
py_script = requests.get("https://raw.githubusercontent.com/dalidia/CMPUT404-lab1/main/request-version.py")
print(py_script.text)