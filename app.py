# import http.client
# import keys

# conn = http.client.HTTPSConnection("api.zoom.us")

# headers = {
#     'authorization': "Bearer {}".format(keys.JWT),
#     'content-type': "application/json"
#     }

# conn.request("GET", "/v2/users?status=active&page_size=30&page_number=1", headers=headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))
import http.client

conn = http.client.HTTPSConnection("api.zoom.us")

payload = "{\"topic\":\"Important\",\"type\":2,\"start_time\":\"2021-01-18T10:00:00Z\",\"duration\":\"30\",\"password\":\"12345\"}"

headers = {
    # 'authorization' : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IlcyZHY1VldVUWkyOV9UWEdBTklHcHciLCJleHAiOjE2MTE1MjIxMjUsImlhdCI6MTYxMDkxNzMyNn0.KUbfA4jNTfm68qoJiHAIC7KHsNQu7NGrVV9tHxKnIAE",
    'authorization' : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOm51bGwsImlzcyI6IlcyZHY1VldVUWkyOV9UWEdBTklHcHciLCJleHAiOjE2MTE0MTg4OTEsImlhdCI6MTYxMDgxNDA5Mn0.0IZTkn_hvoAgAzv-tCr4-m3DqDyp2VTpPJS17pOdZII",
    # 'authorization': "Bearer eyJhbGciOiJIUzUxMiIsInYiOiIyLjAiLCJraWQiOiI4MmJjODg3OC03ZDMwLTQ2ODQtYjhmZi1iMDA3ZTA1YTk5MmUifQ.eyJ2ZXIiOjcsImF1aWQiOiIyYjI4NTk2MzU2MDMzMDBmNTc2ODJmZTc5NjhiM2MyZSIsImNvZGUiOiJjY1FZenhJYmRQX1hNR2JjdDZQUjUyZkdzSFYxcVBJUUEiLCJpc3MiOiJ6bTpjaWQ6a21ualVqNDdRaUNwNnVuM1doeDBwZyIsImdubyI6MCwidHlwZSI6MCwidGlkIjowLCJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJYTUdiY3Q2UFI1MmZHc0hWMXFQSVFBIiwibmJmIjoxNjEwODg5Njg3LCJleHAiOjE2MTA4OTMyODcsImlhdCI6MTYxMDg4OTY4NywiYWlkIjoiQnlfQlRhMGVUREdrMkVReGtfZmRTQSIsImp0aSI6IjgxZjJkYTFhLTAwN2QtNDAyZS1iN2FjLWE2NzRjYjkyOWZlNyJ9.MO2kM00_aX0rnpfpyZTr5koCR03pbulg8E2m034wP4KMzhEXLf60Kk_cLorQEPr8TpwLOHjZdMjUIDnmoL3xHA",
    'content-type': "application/json"
    }

conn.request("POST", "/v2/users/me/meetings", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))