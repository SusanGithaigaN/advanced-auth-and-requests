import requests
from datetime import datetime

TOKEN = "jhbwuie7wjsdjsbhvd8ajw"
USERNAME = "susan-n-githaiga"
GRAPH_ID = "mygraph01"

pixela_endpoint = "https://pixe.la/v1/users"
# create pixela account & secret token
user_params = {
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# params
graph_config = {
    "id": GRAPH_ID,
    "name": "Driving graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN":  TOKEN
}

# # make POST Request
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# post a pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# option 2
today = datetime(year=2023, month=7, day=23)
# ref: https://www.w3schools.com/python/python_datetime.asp
# print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4.0"
}

# pixel_res = requests.post(pixel_endpoint, json=pixel_config, headers=headers)
# print(pixel_res.text)