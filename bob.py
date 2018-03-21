import time
import os,json
from socket import *
import random

tcp = socket(AF_INET,SOCK_STREAM)
TEMP = ''
DICT = {}
SECT={}


tcp.connect(('localhost',2222))
tcp.send('NEGOCIATION')

msg = tcp.recv(1024)
TEMP = json.loads(msg)

a = random.randint(1,35535)


p = TEMP['p']


g = TEMP['base']


B = (int(g)**a)%int(p)
print "The shared secret of Bob is %d : " % (B)
DICT = {'B':B}
tcp.send(json.dumps(DICT))


msg = tcp.recv(1024)
TEMP = json.loads(msg)
A = TEMP['A']


s = (A**a)%p

print("wait for calculations to be completed !!!!<<<<<<>>>>>")

time.sleep(3)

print "The secret key  is %d " % (s)

SECT = {'S':s}
tcp.send(json.dumps(SECT))