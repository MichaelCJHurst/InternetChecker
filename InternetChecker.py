#!/usr/bin/python3
# coding: Latin-1
"""
Internet Checker
Checks the state of internet connection every 30 seconds
"""
import os
import sys
import time
import urllib.request
import urllib.error
from   configparser import SafeConfigParser

def main():
	""" Where the program starts """
	connected = False
	# Get the values from the config file
	config = read_config()
	# Do the infinite(ish) internet check loop
	while True:
		connected = check_connection(connected, config)
		time.sleep(30)

def read_config():
	""" Reads the contents of the config file """
	parser = SafeConfigParser()
	config = {}
	parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), "InternetChecker.ini"))
	# Connections
	config["closeOnConnect"]    = string_to_bool(parser.get("connections", "closeOnConnect"))
	config["closeOnDisconnect"] = string_to_bool(parser.get("connections", "closeOnDisconnect"))
	config["closeOnChange"]     = string_to_bool(parser.get("connections", "closeOnChange"))
	return config

def string_to_bool(test_string):
	""" Changes a string value to a boolean """
	return bool(test_string in ["True", "true", "Yes", "yes", "Y", "y"])

def check_connection(connected, config):
	""" Returns if there is an internet connection """
	try:
		urllib.request.urlopen("https://www.google.co.uk").close()
	except urllib.error.URLError:
		if connected is True:
			connected = False
			on_disconnected()
			if config["closeOnDisconnect"] is True or config["closeOnChange"] is True:
				sys.exit()
	else:
		if connected is False:
			connected = True
			on_connected()
			if config["closeOnConnect"] is True or config["closeOnChange"] is True:
				sys.exit()
	return connected

def on_connected():
	""" Runs the commands in the OnConnected text file """
	print("Connected")
	file = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "OnConnected.txt"), "r")
	for command in file.readlines():
		if command.strip() != "":
			os.system(command)

def on_disconnected():
	""" Runs the commands in the OnDisconnected text file """
	print("Disconnected")
	file = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "OnDisconnected.txt"), "r")
	for command in file.readlines():
		if command.strip() != "":
			os.system(command)

if __name__ == "__main__":
	main()
