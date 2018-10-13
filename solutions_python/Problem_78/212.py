#!/usr/bin/python
# Google Code Jam 2011, Round 1A: FreeCell Statistics

import sys

def gcd(x,y):
	if x < y:
		return gcd(y,x)
	else:
		if y == 0:
			return x
		return gcd(y, x%y)

T = int(sys.stdin.readline())
for case in xrange(1,T+1):
	n, pd, pg = map(int, sys.stdin.readline().split())
	if pg == 100:
		if pd == 100:
			result = 'Possible'
		else:
			result = 'Broken'
	elif pg == 0:
		if pd == 0:
			result = 'Possible'
		else:
			result = 'Broken'
	else:
		games_d = 100 // gcd(pd, 100)
		if games_d <= n:
			result = 'Possible'
		else:
			result = 'Broken'


	print 'Case #{0}: {1}'.format(case, result)
