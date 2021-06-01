from urllib.parse import urlencode
import requests
import json
import os

AUTHORIZATION_URL = 'https://zoom.us/oauth/authorize'
TOKEN_URL = 'https://zoom.us/oauth/token'
CLIENT_ID = 'kmnjUj47QiCp6un3Whx0pg'
REDIRECT_URI = 'http://localhost:5000/redirect_url'
REFRESH_TOKEN = 'eyJhbGciOiJIUzUxMiIsInYiOiIyLjAiLCJraWQiOiI1MTM5ZTViZC1kOWQyLTQ5Y2ItODEwYi1iNTVlMzIyNWI5MzIifQ.eyJ2ZXIiOjcsImF1aWQiOiIyYjI4NTk2MzU2MDMzMDBmNTc2ODJmZTc5NjhiM2MyZSIsImNvZGUiOiJwaW85bjJ1Qm9NX1hNR2JjdDZQUjUyZkdzSFYxcVBJUUEiLCJpc3MiOiJ6bTpjaWQ6a21ualVqNDdRaUNwNnVuM1doeDBwZyIsImdubyI6MCwidHlwZSI6MSwidGlkIjoxNCwiYXVkIjoiaHR0cHM6Ly9vYXV0aC56b29tLnVzIiwidWlkIjoiWE1HYmN0NlBSNTJmR3NIVjFxUElRQSIsIm5iZiI6MTYxMjEwNDYzOCwiZXhwIjoyMDg1MTQ0NjM4LCJpYXQiOjE2MTIxMDQ2MzgsImFpZCI6IkJ5X0JUYTBlVERHazJFUXhrX2ZkU0EiLCJqdGkiOiI1ZTgwMjdmYy05NjBiLTRkZjgtYWYyMi04NzZlNDY3ZWY2Y2QifQ.1oaWlah6Lzo-x8n2kWPZYNRXJL6ocBWpnhoQPmTxD9zx84NXHN8tnOkVvceM8HLChreD4fvRk_szNxFH4CUKTw'


# Getting authorization from user
def get_authorization_code():
    query_params = {'response_type': 'code', 'client_id': CLIENT_ID, 'redirect_uri': REDIRECT_URI}
    params_encoded = urlencode(query_params)
    print(AUTHORIZATION_URL + '?' + params_encoded)


# Getting access token from authorization server
def get_token():
    query_params = {'grant_type': 'authorization_code', 'code': 'pio9n2uBoM_XMGbct6PR52fGsHV1qPIQA',
                    'redirect_uri': REDIRECT_URI}
    headers = {
        'authorization': "Basic a21ualVqNDdRaUNwNnVuM1doeDBwZzo4ek5Na1pHTWMwd3lBc0J3VG9TSHMzVjZvNTRIbVJWRA=="
        # 'content-type': "application/json"
    }
    oauth_token = requests.post(TOKEN_URL, params=query_params, headers=headers)
    print(oauth_token.json().get('access_token'))
    print(oauth_token.json().get('refresh_token'))
    # os.environ['ZOOM_REFRESH_TOKEN'] = oauth_token.json().get('access_token')


# Refreshing access token
def refresh_token():
    # zoom_refresh_token = os.environ.get('ZOOM_REFRESH_TOKEN')
    query_params = {'grant_type': 'refresh_token', 'refresh_token': REFRESH_TOKEN}
    headers = {
        'authorization': "Basic a21ualVqNDdRaUNwNnVuM1doeDBwZzo4ek5Na1pHTWMwd3lBc0J3VG9TSHMzVjZvNTRIbVJWRA=="
        # 'content-type': "application/json"
    }
    response = requests.post(TOKEN_URL, params=query_params, headers=headers)
    print(response.json().get('access_token'))
    print(response.json().get('refresh_token'))

    # zoom_access_token = response.json().get('access_token')
    # zoom_refresh_token = response.json().get('refresh_token')
    #
    # os.environ['ZOOM_ACCESS_TOKEN'] = zoom_access_token
    # os.environ['ZOOM_REFRESH_TOKEN'] = zoom_refresh_token


def create_meeting():
    # conn = http.client.HTTPSConnection("api.zoom.us")
    # payload = '{{"topic":"{}","type":{},"start_time":"{}","duration":{},"password":"{}"}}'.format(
    #     topic, type, start_time, duration, password)
    payload = {
        "topic": "important",
        "type": 2,
        "duration": 30,
        "start_time": "2021-02-29T10:00:00Z"
    }

    headers = {
        "authorization": "Bearer eyJhbGciOiJIUzUxMiIsInYiOiIyLjAiLCJraWQiOiIzNmMyZWQ3Yi0yMzNkLTQ1NmUtOGZiYS0zM2VmNTI4ODkwMzgifQ.eyJ2ZXIiOjcsImF1aWQiOiIyYjI4NTk2MzU2MDMzMDBmNTc2ODJmZTc5NjhiM2MyZSIsImNvZGUiOiJwaW85bjJ1Qm9NX1hNR2JjdDZQUjUyZkdzSFYxcVBJUUEiLCJpc3MiOiJ6bTpjaWQ6a21ualVqNDdRaUNwNnVuM1doeDBwZyIsImdubyI6MCwidHlwZSI6MCwidGlkIjoxMCwiYXVkIjoiaHR0cHM6Ly9vYXV0aC56b29tLnVzIiwidWlkIjoiWE1HYmN0NlBSNTJmR3NIVjFxUElRQSIsIm5iZiI6MTYxMjAxOTU1NiwiZXhwIjoxNjEyMDIzMTU2LCJpYXQiOjE2MTIwMTk1NTYsImFpZCI6IkJ5X0JUYTBlVERHazJFUXhrX2ZkU0EiLCJqdGkiOiI4MmFlZGQyYy1iNjY0LTRlZjAtYWU2Yi0xN2Q2NzBkYjRlZGMifQ.LVIqFK4-AWkhEOr3NEVSeve6Xj0SIzUlaoNuivrKGBYt5WO6mf8MfJUrOjzWnflYDouWocxGjtInr3Ms689jZQ",
        "content-type": "application/json"
    }
    response = requests.post("https://api.zoom.us/v2/users/XMGbct6PR52fGsHV1qPIQA/meetings", data=json.dumps(payload),
                             headers=headers)
    print(response.json().get('start_url'))
    # conn.request(
    #     "POST", "/v2/users/XMGbct6PR52fGsHV1qPIQA/meetings", payload, headers)
    #
    # res = conn.getresponse()
    # data = res.read().decode("utf-8")
    # return data


# get_authorization_code()
# get_token()
refresh_token()
# create_meeting()
# os.environ['ZOOM_REFRESH_TOKEN'] = REFRESH_TOKEN
# zoom_refresh_token = os.environ.get('ZOOM_REFRESH_TOKEN')
# print(zoom_refresh_token)
# os.environ['ZOOM_REFRESH_TOKEN'] = '123'
# zoom_refresh_token = os.environ.get('ZOOM_REFRESH_TOKEN')
# print(zoom_refresh_token)
# zoom_refresh_token = REFRESH_TOKEN
# print(zoom_refresh_token)
# os.system("SETX {0} {1}".format(ZOOM_REFRESH_TOKEN, REFRESH_TOKEN))
# command = 'set ZOOM_REFRESH_TOKEN="eyJhbGciOiJIUzUxMiIsInYiOiIyLjAiLCJraWQiOiJlNGRlYjQ1Ni1jZjA5LTQ0ZTMtOWMxNy03MzkzZDRhNzY2NzUifQ.eyJ2ZXIiOjcsImF1aWQiOiIyYjI4NTk2MzU2MDMzMDBmNTc2ODJmZTc5NjhiM2MyZSIsImNvZGUiOiIxS2hLQklrMmpYX1hNR2JjdDZQUjUyZkdzSFYxcVBJUUEiLCJpc3MiOiJ6bTpjaWQ6a21ualVqNDdRaUNwNnVuM1doeDBwZyIsImdubyI6MCwidHlwZSI6MCwidGlkIjowLCJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJYTUdiY3Q2UFI1MmZHc0hWMXFQSVFBIiwibmJmIjoxNjExNDgyMDkwLCJleHAiOjE2MTE0ODU2OTAsImlhdCI6MTYxMTQ4MjA5MCwiYWlkIjoiQnlfQlRhMGVUREdrMkVReGtfZmRTQSIsImp0aSI6IjY4NWZhYWU3LTczNTctNDkxZS1iYTc5LTNhZDVjOGEzYmFkMSJ9.uPIn_1XUC61kp8lvEWIu8wfj2AVBRWbmHQEhGjZTu2Uj29Q0skaKkagGGshdNOzZGKwuoHlnq1PyALvojQfnIw"'#
# os.system(command)
# os.system('set ZOOM_REFRESH_TOKEN')