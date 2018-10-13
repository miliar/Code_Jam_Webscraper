#!/usr/bin/python

from sys import argv
input = file( argv[1] )

# define problem vars
n = input.next().strip()	# Number of test cases

# helper functions
def run_test( input ):
	n = int( input.next() )
	product = 0

	if n == 0: return 0

	scalar1 = input.next().strip().split( ' ' )
	scalar2 = input.next().strip().split( ' ' )

	scalar2b, scalar1b = [], []

	for s in scalar1: scalar1b.append(int(s))
	for s in scalar2: scalar2b.append(int(s))

	scalar1b.sort()
	scalar2b.sort()
	scalar2b.reverse()

	for i in range( n ):
		product += int( scalar1b[i] ) * int( scalar2b[i] )

	return product

# run tests
for i in range( 1, int(n) + 1 ): 
	print "Case #%s: %s" % ( i, run_test( input ) )

