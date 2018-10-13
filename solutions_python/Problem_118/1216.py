#!/usr/bin/env python2.7

import math

def solve(filename):
	inf = open(filename, "Ur")
	ouf = open("out", "w")
	l = inf.readlines()
	num = int(l.pop(0))
	for n in range(num):
		(b, t) = map(lambda x: long(x) ** (0.5), l[n].split())
		b = long(math.ceil(b))
		t = long(math.floor(t))
		count = 0
		pos = b
		while pos <= t:
			if pal(pos) and pal(pos ** 2): 
				count += 1
			pos += 1
		ouf.write("Case #" + str(n + 1) + ": " + str(count) + "\n")	

def pal(x):
	s = str(x)
	l = len(s)
	for n in range(int(math.ceil(l / 2))):
		if s[n] != s[l - n - 1]: return False
	return True

solve("in3")
