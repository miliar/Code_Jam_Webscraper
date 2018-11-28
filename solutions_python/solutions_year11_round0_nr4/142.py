#! /usr/bin/python

import sys

f = open(sys.argv[1], "rt")

for t in range(int(f.readline())):
	n = int(f.readline()) 
	l = map(int, f.readline().split(' '))

	c = len(l)
	for i in range(len(l)):
		if (l[i] == i+1):
			c -= 1	

	print 'Case #' + str(t+1) + ': ' + str(c)
