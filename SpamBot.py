from os import system
import threading
import requests, random
from colorama import Fore
proxies = open("proxy.txt").read().splitlines()

def getProxy():
    return random.choice(proxies)

def main():	
	system("cls && title = pastehub.net spammer by cvip")

	spam = 0

	url = "https://pastehub.net/create.php"

	title = input("What do you want the title to be> ")
	test = input("What do you want the text to say> ")

	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
		'title': title,
		'syntax': 'plain',
		'expire': '2147483647',
		'visibility': 'public',
		'content': test
	}

	while True:
		requests.post(url, data=headers, proxies={"http": 'http://' + getProxy()})
		spam += 1
		print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] title = {title} : text = {test} : proxy = {getProxy()} : amount sent = " + str(spam))

threading.Thread(target= main()).start()