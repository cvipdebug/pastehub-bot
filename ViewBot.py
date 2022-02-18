from os import system
import requests, random, threading
from colorama import Fore
proxies = open("proxy.txt").read().splitlines()

def getProxy():
    return random.choice(proxies)
def main():
    views = 0
    system("cls && title = pastehub.net view bot by cvip")
    id = input("Put the id of the past here> ")

    url = f"https://pastehub.net/{id}"


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',
    }

    while True:
        requests.post(url, data=headers, proxies={"http": 'http://' + getProxy()})
        views += 1
        print("["+Fore.GREEN+"INFO"+Fore.WHITE+f"] Sent {getProxy()} to {url} : views sent = " + str(views))

threading.Thread(target= main()).start()
