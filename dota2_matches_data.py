import urllib.request
import json

url = ' https://api.opendota.com/api/proMatches'
# with urllib.request.urlopen('https://api.opendota.com/api/proMatches') as f:
#     f.read(100)
json_obj = urllib.request.urlopen(url)
data = json.load(json_obj)
for item in data:
    print(item['duration'] / 60 / 60)
