#!/usr/bin/env python

import sys

def gcd(a, b):
	x, y = min(a,b),max(a,b)
	while x:
		r = y%x
		y = x
		x = r
	return y

def possib(n, p):
	d = gcd(p, 100)
	t = 100/d
	w = p/d
	return [(w*i,t*i) for i in range(1,n/t+1)]

T = int(sys.stdin.readline().strip())

for i in range(0, T):
	N, Pd, Pg = [int(x) for x in sys.stdin.readline().split()]
	
	if Pg == 0 and Pd != 0:
		print "Case #%d: Broken"%(i+1)
		continue
	if Pg == 100 and Pd != 100:
		print "Case #%d: Broken"%(i+1)
		continue
	if len(possib(N, Pd)) == 0:
		print "Case #%d: Broken"%(i+1)
		continue
	print "Case #%d: Possible"%(i+1)

