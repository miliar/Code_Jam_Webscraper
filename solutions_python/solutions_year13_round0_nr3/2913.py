#!/usr/bin/python
import string
import operator
def ReverseNumber(n, partial=0):
	if n == 0:
		return partial
	return ReverseNumber(n / 10, partial * 10 + n % 10)
def solve(a, b):
	x = 0
	for i in xrange(a, b+1):
		if(i == ReverseNumber(i)):
			radical = i**(0.5)
			if((int(radical) * int(radical)) == i):
#				print i, radical, ReverseNumber(radical)
				if(int(radical) == ReverseNumber(int(radical))):
					x = x + 1
	return x
f = open('C-small-attempt0.in', 'r');
l1 = f.readline();
T = int(l1)
for i in xrange(1,T+1):
	l1 = f.readline()
	l1 = l1.split(' ')
	a = int(l1[0])
	b = int(l1[1])
	print "Case #"+str(i)+": "+str(solve(a, b))
