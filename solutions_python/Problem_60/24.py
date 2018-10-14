#!/usr/bin/python
# Author: Ivan Kazmenko
import sys
tests = int (sys.stdin.readline ())
for test in range (tests):
	n, k, b, t = [int (z) for z in sys.stdin.readline ().split ()]
	x = [int (z) for z in sys.stdin.readline ().split ()]
	v = [int (z) for z in sys.stdin.readline ().split ()]
	d = [x[i] + v[i] * t >= b for i in range (n)]
	if sum (int (z) for z in d) < k:
		s = 'IMPOSSIBLE'
	else:
		s = 0
		p = [sum (int (not z) for z in d[i:]) for i in range (n)]
		a = []
		for i in range (n):
			if d[i]:
				a += [p[i]]
		a.sort ()
		s = sum (a[:k])
	sys.stdout.write ('Case #%d: %s\n' % (test + 1, str (s)))
