#!/usr/bin/env python
# -*- coding: utf8 -*-

__author__    = "renaud blanch <rndblnch at gmail dot com>"
__copyright__ = "Copyright © 2010 - Renaud Blanch"
__licence__   = "GPLv3 [http://www.gnu.org/licenses/gpl.html]"

import sys
next_line = sys.stdin.next


"""
Rotate
[http://code.google.com/codejam/contest/dashboard?c=544101#s=p0]
"""

def row(N, K, board):
	board = ["".join(reversed(l.replace(".", ""))) for l in board]
	board = [''.join([l, " "*(N-len(l))]) for l in board]
	B, R = False, False
	B_row, R_row = 'B' * K, 'R' * K
	for col in board:
		B |= B_row in col
		R |= R_row in col
	lines = [''.join(l) for l in zip(*board)]
	for line in lines:
		B |= B_row in line
		R |= R_row in line
	diag = [''.join([' '*i, l]) for i, l in enumerate(board)]
	diag = [''.join(l) for l in zip(*diag)]
	for line in diag:
		B |= B_row in line
		R |= R_row in line
	diag = [''.join([' '*(N-i), l]) for i, l in enumerate(board)]
	diag = [''.join(l) for l in zip(*diag)]
	for line in diag:
		B |= B_row in line
		R |= R_row in line
	if R:
		res = 'Both' if B else 'Red'
	else:
		res = 'Blue' if B else 'Neither'
	return res
	
T = int(next_line())
for X in xrange(T):
	print "Case #%s:" % (X+1),
	N, K = [int(w) for w in next_line().split()]
	board = [next_line().strip() for _ in xrange(N)]
	print row(N, K, board)
