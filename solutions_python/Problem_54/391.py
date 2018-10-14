#!/usr/bin/python

import sys

def egcd(a, b):
	x, lx = 0, 1
	y, ly = 1, 0
	while b:
		qt=a//b
		a,b=b,a%b
		x,lx=lx-qt*x, x
		y,ly=ly-qt*y, y
	return a

file = open(sys.argv[1])
text = file.read()
file.close()
lines = text.split("\n")
LN = int(lines[0])

case = []

for line in lines[1:-1]:
	seps = line.split(' ')
	N = int(seps[0])
	t = []
	for i in range(N):
		t.append(int(seps[i+1]))
	k = abs(t[0]-t[1])
	for i in range(1,N):
		k=egcd(k,abs(t[i-1]-t[i]))

	ok=1
	for i in t:
		if(i%k!=0):
			ok=0
			break

	if ok:
		case.append(0)
	else:
		case.append(k-(t[0]%k))

for i in range(len(case)):
	print "Case #"+str(i+1)+": "+str(case[i])
