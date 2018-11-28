#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
	print 'Need Input!'
	sys.exit()

f=open(sys.argv[1],'r')
numcases = int(f.readline())
for i in range(1, numcases+1):
	print "Case #" + str(i) + ": ",
	numengines = int(f.readline())
	engines = []
	for j in range(0, numengines):
		engines.append(f.readline())
	numqueries = int(f.readline())
	switches = 0
	seen = 0L
	for j in range(0, numqueries):
		q = f.readline()
		ind = engines.index(q)
		seen = seen | (2**ind)
		if (seen == (2**numengines - 1)):
			switches = switches + 1
			seen = 2**ind
	print switches
