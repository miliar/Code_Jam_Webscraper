#!/usr/bin/env python

import sys

t = int(sys.stdin.readline())

for i in range(t):
	line = sys.stdin.readline().split(' ');
	n = int(line[0])
	k = int(line[1])

	npow= 2**n

	k = k % (npow) 

	if (npow - k == 1):
		print "Case #%i: ON" % (i+1)
	else:
		print "Case #%i: OFF" % (i+1)

