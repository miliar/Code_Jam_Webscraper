#!/usr/bin/python
import sys

def euclid (a, b):
	if a == 0 or b == 0:
		return a + b
	return euclid (b, a % b)

s = sys.stdin.readline ()
tests = int (s)
for test in range (tests):
	s = sys.stdin.readline ()

	t = [int (x) for x in s.split ()]
	n = len (t) - 1
	assert n == t[0]
	t = t[1:]

	d = 0
	for i in range (1, n):
		d = euclid (d, abs (t[i] - t[0]))
	k = t[0] % d
	k = (d - k) % d

	sys.stdout.write ('Case #%d: %d\n' % (test + 1, k))
