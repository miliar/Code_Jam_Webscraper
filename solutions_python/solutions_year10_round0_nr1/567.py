#!/usr/bin/python

import sys

def snapper(n,k):
	return ( ( k & ( (1<<n) - 1) ) == ( (1<<n) - 1) )

num_entries = input()
entries = []
c = 0

while c < num_entries:
	s = sys.stdin.readline()
	entries.append(map(int, s.split(' ')))
	c += 1

c = 0
while c < num_entries:
	if snapper(entries[c][0], entries[c][1]):
		print "Case #" + str(c+1) + ": ON"
	else:
		print "Case #" + str(c+1) + ": OFF"
	c += 1
