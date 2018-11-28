#!/usr/bin/python

def theWinnerIs(x, r, c):
	
	if x > 6:
		# Richard can choose an "holed" X-omino
		return "RICHARD"
	
	if 1 in [r,c] and x > 2:
		# The grid is single-dimension and the x-omino can lay on 2-dimensions.
		return "RICHARD"
	
	if r * c % x != 0 or r * c < x:
		# The grid is wrong...
		return "RICHARD"
	
	if min(r, c) == 2 and x == 4:
		return "RICHARD"
	
	return "GABRIEL"

T = int(raw_input())

for t in xrange(T):
	x, r, c = map(int, raw_input().split())
	print "Case #%d: %s" % (t+1, theWinnerIs(x, r, c) )