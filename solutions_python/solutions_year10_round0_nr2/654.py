#!/usr/bin/python
from sys import *
from string import *
import math

def euclid(a,b):
	A = a
	B = b
	while B>0:
		t = A
		A = B
		B = t%B
	return A


C = int(stdin.readline().strip())
for i in range(C):
	s = stdin.readline().strip().split()
	X = []
	slen = len(s)
	for j in range(1,slen):
		X.append(long(s[j]))
	X.sort()
	Y = []
	for k in range(slen-2):
		Y.append(X[k+1]-X[k])	
	gcd = Y[0]
	for l in range(1,slen-2):
		gcd = euclid(gcd,Y[l])
	ans = gcd * long(math.ceil(float(X[0])/float(gcd))) - X[0]
	if ans < 0:
		ans = ans + gcd
	print "Case #" + str(i+1) + ": " + str(ans)
