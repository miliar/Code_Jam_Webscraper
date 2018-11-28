#!/usr/bin/env python

import sys, heapq
from heapq import heappush, heappop

def solve(case, events):
	a = 0
	b = 0
	a_start = 0
	b_start = 0
	for i in xrange(len(events)):
		e = heappop(events)
		if (e[1] == "A DEPART"):
			if (a == 0):
				a_start += 1
			else:
				a -= 1
		elif (e[1] == "B DEPART"):
			if (b == 0):
				b_start += 1
			else:
				b -= 1
		elif (e[1] == "A READY"):
			a += 1
		elif (e[1] == "B READY"):
			b += 1
	print "Case #%d: %d %d" % (case, a_start, b_start)


if (len(sys.argv) < 2):
	print "usage: tt.py <infile>"
	sys.exit(1)

f = open(sys.argv[1], 'r')

cases = (int) (f.readline().strip())
for case in xrange(cases):
	turnaround = (int) (f.readline().strip())
	nums = f.readline().split()
	num_AB = (int) (nums[0])
	num_BA = (int) (nums[1])
	events = []
	for trip in xrange(num_AB):
		line = f.readline()
		hours = (int) (line[0:2])
		minutes = (int) (line[3:5])
		depart = hours * 60 + minutes
		heappush(events, (depart+.1, "A DEPART"))
		hours = (int) (line[6:8])
		minutes = (int) (line[9:11])
		ready = hours * 60 + minutes + turnaround
		heappush(events, (ready, "B READY"))
	for trip in xrange(num_BA):
		line = f.readline()
		hours = (int) (line[0:2])
		minutes = (int) (line[3:5])
		depart = hours * 60 + minutes
		heappush(events, (depart+.1, "B DEPART"))
		hours = (int) (line[6:8])
		minutes = (int) (line[9:11])
		ready = hours * 60 + minutes + turnaround
		heappush(events, (ready, "A READY"))
	solve(case+1, events)


