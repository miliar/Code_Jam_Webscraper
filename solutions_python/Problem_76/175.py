#!/usr/bin/python

T = int(raw_input())
for t in xrange(T):
	n = int(raw_input())
	V = map(int, raw_input().split())
	print "Case #%d:" % (t + 1),
	if reduce(lambda x, y: x^y, V) != 0:
		print "NO"
	else:
		print sum(V) - min(V)

