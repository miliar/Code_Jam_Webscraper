#!/bin/python
import os, sys
T = int(raw_input())
p = sys.stdout.write

for c in xrange(1, T + 1):
	
	s = 2.0
	e = 0.0

	p('Case #%d: '  % c)
	C, F, X = map(float, raw_input().split())

	while True:
		t1 = X / s
		t2 = C / s + X / ( s + F )

		if t1 < t2: 
			break

		e += C / s
		s += F
	
	p('%.7f\n' % (t1 + e))
