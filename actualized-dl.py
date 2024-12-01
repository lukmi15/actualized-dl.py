#!/usr/bin/env python3

#Downloading the audio versions of all Actualized.org videos for safe keeping
#Author(s)		: Lukas Mirow
#Date of creation	: 2024-12-01


import requests
from sys import stderr


USER_AGENT = "actualized-dl.py (https://github.com/lukmi15/actualized-dl.py)"
XML_PATH = "itunes.xml"
XML_URI = f"https://actualized.org/{XML_PATH}"
DONT_CHECK_AUDIO_CERTS = True #Unfortunately, the cert for actualizedfiles.com expired


def err(msg, exit_code = 1):
	print(f"Error: {msg}", stderr)
	exit(exit_code)

def download_file(url):
	response = requests.get(url)
	if response.status_code != 200:
		err(f"Expected return code `200`, got `{response.status_code}`")
	with open(XML_PATH, "w") as f:
		f.write(response.text)


if __name__ == "__main__":
	print("===== Downloading `itunes.xml` =====")
	download_file(XML_URI)
	# print("===== Downloading audios =====")
	# download_audios() #TODO
	print("===== Done =====")
