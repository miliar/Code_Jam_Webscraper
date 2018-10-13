#!/usr/bin/env python
# -*- coding: utf8 -*-

__author__    = "renaud blanch <rndblnch at gmail dot com>"
__copyright__ = "Copyright © 2010 - Renaud Blanch"
__licence__   = "GPLv3 [http://www.gnu.org/licenses/gpl.html]"

import sys
next_line = sys.stdin.next


"""
Magicka
[http://code.google.com/codejam/contest/dashboard?c=975485#s=p1]
"""

from collections import defaultdict

BASES = "QWERASDF"

def invoke(combine, opposed, l):
	r = " "
	for c in l:
		while True:
			last = r[-1]
			if last+c in combine:
				r = r[:-1]
				c = combine[last+c]
			else:
				break
		if c in opposed:
			if opposed[c] & set(r):
				r, c = "", " "
		r = r+c
	return '[' + ", ".join(r[1:]) + ']'



T = int(next_line())
for X in xrange(T):
	print "Case #%s:" % (X+1),
	l = next_line().strip()
	
	C, l = l.split(None, 1)
	combine = {}
	for _ in xrange(int(C)):
		c, l = l.split(None, 1)
		a, b, r = c
		combine[a+b] = combine[b+a] = r
	

	D, l = l.split(None, 1)
	opposed = defaultdict(set)
	for _ in xrange(int(D)):
		o, l = l.split(None, 1)
		a, b = o
		opposed[a].add(b)
		opposed[b].add(a)
	
	N, l = l.split(None, 1)
	assert len(l) == int(N)
	
	print invoke(combine, opposed, l)
