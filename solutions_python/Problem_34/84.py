#!/usr/bin/python

import re

L,D,N = tuple(int(i) for i in raw_input().split())

words = [""] * D

for i in xrange(D):
	words[i] = raw_input().strip()
	
for i in xrange(N):
	K = raw_input().strip().replace("(","[").replace(")","]")
	matches = 0
	for j in words:
		if re.match(K,j): matches += 1
	
	print "Case #%d: %d" % (i + 1, matches)