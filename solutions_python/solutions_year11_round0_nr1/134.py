#! /usr/bin/python

import sys
from collections import deque

f = open(sys.argv[1], "rt")

for x in range(int(f.readline())):
	
	l = f.readline().split(' ')
	l = zip(l[1::2], map(int,  l[2::2]))
	
	t = 0
	d = {'O' : (0, 1) , 'B': (0, 1)} #time, pos
	for bot, p in l:
		t0, p0 = d[bot]
		t += max(0, abs(p0 - p) - (t-t0)) + 1
		d[bot] = (t, p)
	print 'Case #' + str(x+1) + ': ' + str(t)
