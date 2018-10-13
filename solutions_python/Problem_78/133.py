#!/usr/bin/python

import sys
from fractions import gcd

f = open("a.in","rb")
t = int(f.readline())

def check(n,pd,pg):
	di = gcd(pd,100)
	a = pd/di
	b = 100/di
	if (a>n or b>n):
		return 0
	if (pg == 100):
		if (pd < 100):
			return 0
	if (pg == 0):
		if (pd > 0):
			return 0
	return 1

for i in range(t):
	s = map(int,f.readline().split())
	n,pd,pg = s[0],s[1],s[2]

	if (check(n,pd,pg) == 1):
		print "Case #"+str(i+1)+": Possible"
	else:
		print "Case #"+str(i+1)+": Broken"
