#!/usr/bin/env python

import sys

def debug(*args):
	""" Debug function"""
#	print args

def recycled(n, m):
	n, m = str(n), str(m)
	if n == m:
		return False
	if len(n) != len(m):
		return False
	if n.startswith("0") or m.startswith("0"):
		return False
	for i in range(1, len(n)):
		recycled_n = n[-i:] + n[0:len(n) -i ]
		#debug("recicled", m, n, recycled_n)
		if m == recycled_n:
			return True
	return False


lines = sys.stdin.readlines()
case = 1
for line in lines[1:]:
	#debug("line", line)
	a, b = [int(x, 10) for x in  line.split(' ')]
	count = 0
	for n in range(a, b+1):
		debug("a,b", a, b)
		for m in range(n, b+1):
			debug("n,m", n, m)
			if n < m and recycled(n, m):
				count += 1
	print "Case #%d: %d" % (case, count)
	case += 1
