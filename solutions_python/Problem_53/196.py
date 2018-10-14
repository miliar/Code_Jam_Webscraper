#!/usr/bin/python
import sys

file = open(sys.argv[1])
text = file.read()
file.close()

lines = text.split("\n")

total = int(lines[0])

case = []

for i in range(1,total+1):
	a = lines[i].split(' ')
	N = int(a[0])
	K = int(a[1])
	if(bin(K)[-N:].find('0') == -1 and bin(K)[-N:].find('b') == -1):
		case.append(1)
	else: 
		case.append(0)

for i in range(len(case)):
	if(case[i]==1):
		t = 'ON'
	else:
	 	t = 'OFF'
	print 'Case #'+str(i+1)+': '+t

