#!/usr/bin/python

# k - people at once
# r - times a day

# input:
# t - test cases
# r k n
# g1 .. gn

import sys

rl = sys.stdin.readline

for t in xrange(1, int(rl()) + 1):
	r, k, n = map(long, rl().split())
	g = map(int, rl().split())
	euro = 0
	s = sum(g)

	if (k >= s):
		euro = s * r
	elif (min(g) > k):
		euro = 0
	else:
		for R in xrange(r):
			o = 0

			for N in xrange(n):
				if ((o + g[N]) > k):
					break

				o += g[N]

			if o == 0:
				N = 1

			#print R, o, g[:N]
			g = g[N:] + g[:N]
			euro += o

	print 'Case #%d: %d' % (t, euro)
