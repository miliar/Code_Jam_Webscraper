#!/usr/bin/env python

import sys

T = int(sys.stdin.readline())
for case in xrange(T):
	N,M = [int(x) for x in sys.stdin.readline().split()]
	seen = {}
	for i in xrange(N):
		s = sys.stdin.readline()
		s = s.strip().split('/')[1:]
		c = ""
		for j in s:
			c += "/" + j
			seen[c] = 1
	ret = 0
	for i in xrange(M):
		s = sys.stdin.readline()
		s = s.strip().split('/')[1:]
		c = ""
		for j in s:
			c += "/" + j
			if not seen.has_key(c):
				seen[c] = 1
				ret += 1
	print "Case #%d: %d" % (case+1,ret)