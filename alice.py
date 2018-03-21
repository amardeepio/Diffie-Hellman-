import os,json
from socket import *
import random
import time


print("")
print ("***********************")
print ("*    Diffie Hellman   *")
print ("*     Key Exchange    *")
print ("***********************")

def isPrime(n):
	c=0
	for i in range(1,n):
		if n%i == 0:
			c=c+1
	if c == 1:
		return True


prime = 1

while True:
	prime = random.randint(100,1000)
	if isPrime(prime) == True:
		
		break
	else :
		prime = prime


while True:
	generator = random.randint(2,prime-2)
	if isPrime(generator) == True:
		break
	else :
		generator = generator





print "prime =",prime     #prime
print "generator =",generator    #generator

a = random.randint(1,35535)


tcp = socket(AF_INET,SOCK_STREAM)
tcp.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp.bind(('localhost',2222))
tcp.listen(5)
TEMP = {}
FOO = ''
BAR = ''

TEMP = {'p':prime,'base':generator}
conn, addr = tcp.accept()
while 1:
    msg = conn.recv(1024)
    if "NEGOCIATION" in msg:
        conn.send(json.dumps(TEMP)) 
        print "Sending base and prime number..."
        break

A = (generator ** a)% prime

print "the shared secret of alice is: %d  " % (A)

msg = conn.recv(1024)
FOO = json.loads(msg)


B = FOO['B']


s = (B ** a)% prime

TEMP = {'A':A}
conn.send(json.dumps(TEMP))




print("wait for calculations to be completed !!!!<<<<<<>>>>>")

time.sleep(3)

print "The secret is %d " % (s)

msg =conn.recv(1024)
BAR =json.loads(msg)
 
 
secret2= BAR['S']
 
if s == secret2 :
 
    print " keys are verified successfully ! "