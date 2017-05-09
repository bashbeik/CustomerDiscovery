# Script for getting a large batch of emails from linkedin profiles via RocketReach API. 
# Save your Linkedin profile links in 'linkedinlinks.txt' (one link per line). 
# Also you need to fill in your API key in the script.

import requests, json
url = "https://api.rocketreach.co/v1/api/lookupProfile?api_key=[YOUR_API_KEY]&li_url="
lines = [line.rstrip('\n') for line in open('linkedinlinks.txt')]
for line in lines:
    fullurl = url+line
    data = requests.get(fullurl)
    json_data=data.text
    data = json.loads(json_data)
    emails = [item['email'] for item in data[0]['emails']]
    print emails
