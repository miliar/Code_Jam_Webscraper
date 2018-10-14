#!/usr/bin/python

import sys

def coaster(R,k,N,l):
	t=0 # total riders
	for c in range(R): # loop over max runs
		g=0 # num groups boarded this run
		p=0 # num passengers this run
		while (p+l[0]<=k) and (g<N): # passengers <= capacity, groups <= numgroups
			g+=1
			t+=l[0]
			p+=l[0]
			l.append(l.pop(0)) # to the back of the line
	return t

c=0
num_entries = input()
entries = []

while c < num_entries:
	p = sys.stdin.readline()
	g = sys.stdin.readline()
	entries.append(map(int, p.split(' ')))
	entries[-1].append(map(int, g.split(' ')))
	c+=1

c=0
while c < num_entries:
	print "Case #" + str(c+1) + ": " + str(coaster(entries[c][0],entries[c][1],entries[c][2],entries[c][3]))
	c+=1
