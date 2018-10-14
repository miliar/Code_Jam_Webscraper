#!/usr/bin/python

T = int(raw_input())

for tc in range(1, T + 1):
	s = raw_input()
	s = raw_input()
	a = sorted(map(int, s.split()))
	xorsum = 0
	for x in a:
		xorsum ^= x
	if xorsum != 0:
		print "Case #%d: NO" % tc
	else:
		print "Case #%d: %d" % (tc, sum(a) - a[0])

	
