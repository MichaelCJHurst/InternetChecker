# Internet Checker

This checks whether there is an active internet connection every 30 seconds.

## Config

The config file has three options:

- closeOnConnect - whether the application should close when an internet connection is detected
- closeOnDisconnect - whether the application should close when an internet connection is lost
- closeOnChange - whether the application should close when an internet connection is either detected or lost

## OnConnected.txt

When an internet connection is first detected, the commands stored in this file - each on a new line - will be run.

## OnDisconnected.txt

When an internet connection is first lost, the commands stored in this file - each on a new line - will be run.
