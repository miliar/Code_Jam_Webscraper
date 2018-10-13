#!/usr/bin/env python
# -*- coding: utf8 -*-

__author__    = "renaud blanch <rndblnch at gmail dot com>"
__copyright__ = "Copyright © 2010 - Renaud Blanch"
__licence__   = "GPLv3 [http://www.gnu.org/licenses/gpl.html]"

import sys
next_line = sys.stdin.next


"""
Number Game
[http://code.google.com/codejam/contest/dashboard?c=544101#s=p2]
"""

_winnings = {}
def winning(A, B):
	key = (A, B)
	try:
		return _winnings[key]
	except:
		pass
	if B > A:
		return winning(B, A)
	ones = 0
	while B > 0:
		d, m = divmod(A, B)
		if d > 1:
			break
		ones += 1
		A, B = B, m
	res = ((ones % 2) == 0)
	_winnings[key] = res
	return res

def winnings(A1, A2, B1, B2):
	count = 0
	A = A1
	while A <= A2:
		B = B1
		while B <= B2:
			if winning(A, B):
				count += 1
			B += 1
		A += 1
	return count

T = int(next_line())
for X in xrange(T):
	print "Case #%s:" % (X+1),
	A1, A2, B1, B2 = [int(w) for w in next_line().split()]
	print winnings(A1, A2, B1, B2)
