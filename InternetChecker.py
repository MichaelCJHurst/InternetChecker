#!/usr/bin/python3
# coding: Latin-1
"""
Internet Checker
Checks the state of internet connection every 30 seconds
"""
import time
import urllib.request

CONNECTED = False

while True:
	try:
		urllib.request.urlopen("https://www.google.co.uk").close()
	except urllib.error.URLError as ex:
		if CONNECTED is True:
			print("Disconnected")
			CONNECTED = False
	else:
		if CONNECTED is False:
			print("Connected")
			CONNECTED = True
	time.sleep(30)
