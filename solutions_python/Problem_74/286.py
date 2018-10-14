#!/usr/bin/env python
# -*- coding: utf8 -*-

__author__    = "renaud blanch <rndblnch at gmail dot com>"
__copyright__ = "Copyright © 2010 - Renaud Blanch"
__licence__   = "GPLv3 [http://www.gnu.org/licenses/gpl.html]"

import sys
next_line = sys.stdin.next


"""
Bot Trust
[http://code.google.com/codejam/contest/dashboard?c=975485#]
"""

O, B = "O", "B"

other = {
	O: B,
	B: O
}

def seconds(s):
	t = 0
	place = {
		O: 1,
		B: 1,
	}
	idle_time = {
		O: 0,
		B: 0,
	}
	for color, button in s:
		dt = max(0, abs(place[color] - button) - idle_time[color]) + 1
		place[color], idle_time[color] = button, 0
		idle_time[other[color]] += dt
		t += dt
	return t
	

T = int(next_line())
for X in xrange(T):
	print "Case #%s:" % (X+1),
	N, l = next_line().strip().split(None, 1)
	N = int(N)
	s = []
	while l:
		try:
			color, button, l = l.split(None, 2)
		except ValueError:
			color, button = l.split()
			l = False
		s.append((color, int(button)))
	assert len(s) == N
	print seconds(s)
