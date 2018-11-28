#!/usr/bin/env python2.7
from __future__ import print_function

import collections

debug = False

def flip( s, pos, k ):
	for i in range(pos,pos+k):
		if s[i] == '+':
			s[i] = '-'
		elif s[i] == '-':
			s[i] = '+'
		else:
			raise Exception()
			

def solve( s, k ):
	"""
	Input: s is a string of - and +, need to make it all +
	       by flipping k at a time.
	Returns an int for number of flips, or string 'IMPOSSIBLE'.
	"""

	flips = 0
	i = 0

	s = [ c for c in s ]

	for i in range( len(s)-k+1 ):
		if s[i] == '+':
			continue
		elif s[i] == '-':
			flip( s, i, k )
			flips += 1
			if debug: print( 'flipped at pos %d, pattern is now %-30s' % ( i, ''.join(s) ) )
		else: raise Exception()

	if all( [ c == '+' for c in s ] ):
		return flips
	else:
		return 'IMPOSSIBLE'



if __name__ == '__main__':
	#f = open( 'sample_input.txt' )
	import sys
	f = sys.stdin
	
	num = int( f.readline() )
	
	for i in range(num):
		case = i + 1
		y = case
	
		line = f.readline()
		s, k = tuple( line.split() )
	
		k = int(k)
	
		y = solve( s, k )

		print( 'Case #%d: %s' % ( case, y ) )
