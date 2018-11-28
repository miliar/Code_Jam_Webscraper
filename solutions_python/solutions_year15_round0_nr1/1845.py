#!/usr/bin/env python

def ovate(a, m):
	"""whether standing ovation will happen for a public consisting of a[] members of various shyness levels, and m additional friends we brought, who aren't shy"""
	people = a[0] + m
	for i in xrange(1, len(a)):
		if people < i:
			return False
		else:
			people += a[i]
	return True

T = int(raw_input().strip())

for tc in xrange(1, T + 1):
	n, s = raw_input().strip().split()
	a = map(int, list(s))
	
	l = 0
	r = 1001
	while l < r:
		m = (l + r) / 2
		if ovate(a, m):
			r = m
		else:
			l = m + 1
	print "Case #%d: %d" % (tc, l)
