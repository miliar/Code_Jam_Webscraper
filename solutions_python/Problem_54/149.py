#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division

import sys
import fractions

lines = sys.stdin.readlines()

C = int(lines[0])

for c in range(1, C + 1):
	l = lines[c].split()
	N = int(l[0])
	t = [int(x) for x in l[1:]]
	mint = min(t)
	subt = [tt - mint for tt in t]
	answer = "?"
	g = 0
	for tt in subt:
		g = fractions.gcd(g, tt)
	#~ print t
	#~ print g
	#~ print subt
	answer = (g - (t[0] % g)) % g
	print "Case #%d: %s" % (c, answer)

#~ max gcd(t0+X, t1+X, t2+X, t3+X, t4+X, ...)
