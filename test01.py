import os
import json
import requests
import pandas as pd
import time

os.environ["VIRA_API_KEY"] = "3469d6608b2f8646ce514218a0eba49989175ba98bcdc0b898649c052b4b5bf8"
headers = {
    'Authorization': f'Bearer {os.environ["VIRA_API_KEY"]}'
}

data = pd.read_csv('intent_dataset/intents.csv')

for i, row in data.iterrows():
    text = row['intent']

    response = requests.post("http://vira.eb5e3a7cc143455e9aa1.eastus.aksapp.io/dialog/en", headers=headers, json={"text": text})
    session_id = response.json()['session_id']

    response = requests.post("http://vira.eb5e3a7cc143455e9aa1.eastus.aksapp.io/dialog/en", headers=headers, json={"session_id": session_id, 'text': text})
    print(response.json()['response']) 

    time.sleep(1)
