#!/usr/bin/python
import sys

s = sys.stdin.readline ()
tests = int (s)
for test in range (tests):
	s = sys.stdin.readline ()

	n, k = [int (x) for x in s.split ()]
	m = (1 << n) - 1

	sys.stdout.write ('Case #%d: %s\n' % (test + 1, \
	 ['OFF', 'ON'] [int (m & k == m)]))
