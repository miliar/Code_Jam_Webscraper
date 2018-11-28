#!/usr/bin/python

import sys

if len(sys.argv) < 2:
	print "oops"
	sys.exit(1)

f = open(sys.argv[1], "r")

numCases = int(f.readline())

for i in range(numCases):
	size = int(f.readline())
	l = []
	r = []
	for s in f.readline().split():
		l.append(int(s))
	for s in f.readline().split():
		r.append(int(s))
	l.sort()
	r.sort()
	r.reverse()
	k = 0
	for j in range(size):
		k += l[j] * r[j]
	print "Case #" + str(i + 1) + ": " + str(k)
