#!/usr/bin/env python

import sys
import math
s = sys.stdin
#s = open("B-small-attempt0.in", "r")
r = lambda: s.readline().strip()

def isugly(x):
	return x == 0 or x%2 == 0 or x%3 == 0 or x%5 == 0 or x%7 == 0

primes = (2, 3, 5, 7)
for tt in range( 0, int( r() ) ):
	
	digits = r()
	count = 0

	if len(digits) == 1:
		print "Case #%s: %s" % (tt+1, (0,1)[ isugly( int(digits) )] )
		continue

	def test (x, has_null):
		global count

#		print "%s=%s" % ( x, 0 )
		
		if has_null:
			for i in range(0, len(x) - 1):
				if (x[i] == '+' or x[i] == '-' or x[i] == ' ' ) and x[i+1] == '0' and i<len(x)-2 and x[i+2].isdigit():
					x = x[:i+1] + ' ' + x[i+2:];

		y = eval(x)
		if isugly( y ):
			count += 1

	has_null = digits.find('0') != -1
	p = ('+', '-', '')
	case = [ '' for i in range(1, len(digits)) ]

	all = 3**(len(digits)-1)
	test_case = 0
	while True:
		f = test_case
		for i in range(1, len(digits)):
			case [i-1] = p[ f % 3 ]
			f /= 3
		
		x = digits[0]
		for i in range(1, len(digits)):
			if case[i-1] == '' and x == '0':
				x = x.lstrip('0')
			x += case[i-1] + digits[i]
		test( x, has_null )
		test_case += 1
		if test_case == all:
			break
	
	print "Case #%s: %s" % (tt+1, count )