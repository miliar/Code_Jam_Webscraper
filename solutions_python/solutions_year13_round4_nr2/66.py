#!/usr/bin/python

from sys import stdin, stderr
from math import sqrt

def readiline():
	return map(int, stdin.readline().strip().split() )

tests = readiline()[0]

for test_no in xrange(1,tests+1):
	N, P = readiline()
	y = 2
	z = 1
	if P < 2**N:
		n = 2 ** N
		p = P
		while p > n/2:
			n /= 2
			p -= n
			y = 2*y
	else:
		y = 2**N+1

	n = 2 ** N
	p = P
	while p < n:
		n /= 2
		z *= 2

	y -= 2
	z = 2**N-z
	
	print "Case #%d: %d %d" % (test_no, y, z)
