#/usr/bin/env python2.7
from __future__ import print_function

def isTidy( N ):
	N = str(N)

	prev_c = None
	for i, c in enumerate(N):
		if prev_c is None or int(c) >= int(prev_c):
			pass
		else:
			return False
		prev_c = c

	return True

def getUntidyPos( N ):
	N_str = str(N)

	c_prev = None
	for i, c in enumerate(N_str):
		if c_prev is None or int(c) >= int(c_prev):
			pass
		else:
			return i
		c_prev = c

	return None
			



def solve( N ):
	#print( 'trying to solve %40d' % int(N) )
	N_int = int(N)
	N_str = str(N)


	while True:
		i = getUntidyPos( N_int )
		if i is None: break
		diff = int( N_str[i:] ) + 1
		#print( 'Decreasing N by %20d, now: %20d' % ( diff, N_int ) )
		N_int -= diff
		N_str = str(N_int)

	return N_int
		
		


import sys

tests = int( sys.stdin.readline() )

for i in range(tests):
	case = i + 1
	N = sys.stdin.readline().strip()

	y = solve( N )

	print( 'Case #%d: %d' % ( case, y ) )

	
