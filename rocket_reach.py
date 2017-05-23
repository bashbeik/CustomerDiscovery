# Script for getting a large batch of emails from linkedin profiles via RocketReach API. 
# Save your Linkedin profile links in 'linkedinlinks.txt' (one link per line). 
# Also you need to fill in your API key in the script.

import requests, json, time
url = "https://api.rocketreach.co/v1/api/lookupProfile?api_key=[API_KEY]&li_url="
lines = [line.rstrip('\n') for line in open('linkedinlinks.txt')]
fileToWrite = open('emails.txt', 'w')
for line in lines:
    fullurl = url+line
    data = requests.get(fullurl)
    time.sleep(2)
    json_data=data.text
    data = json.loads(json_data)
    try:
        emails = [item['email'] for item in data[0]['emails']]
    except:
        emails = []
    emailText = ''
    for i,email in enumerate(emails):
        if(i == 0):
            emailText = emailText + email
        else:
            emailText = emailText + email + ','
    fileToWrite.write(emailText)
    fileToWrite.write('\n')
    print emails
fileToWrite.close()
