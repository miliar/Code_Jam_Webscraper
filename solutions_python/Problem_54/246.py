#!/usr/bin/env python
import sys

def gcd(a, b):
	while b != 0:
		tmp = a % b
		a = b
		b = tmp
	return a

NC = int(raw_input())

for nc in xrange(1, NC+1):
	a = raw_input()
	l = a.split()
	n = int(l[0])
	l = [int(x) for x in l[1:]]
	#print l, len(l), n
	assert len(l) == n, "Record %d doesn't occur on one line" % nc
	l.sort()
	#print l
	g = l[1] - l[0]
	for i in xrange(n-1):
		g = gcd(g, l[i+1] - l[i])
	print "Case #%d: %d" % (nc, -l[0] % g)
