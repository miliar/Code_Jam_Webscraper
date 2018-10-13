#!/usr/bin/python

import sys
import os
import math

## vector product
def s2prod( n, a, b ):
	a.sort()
	b.sort()
	b.reverse()
	sum = 0
	for i in range( n ):
		sum += a[ i ] * b[ i ]
	return sum

f = open( sys.argv[ 1 ] )
t = f.readlines()
f.close()

count = 0

for i in range( 1, len( t ), 3 ):
	n = int( t[ i ] )
	v1 = [ int( x ) for x in t[ i + 1 ].strip().split() ]
	v2 = [ int( x ) for x in t[ i + 2 ].strip().split() ]
	sys.stdout.write( "Case #%d: %d\n" % ( count + 1, s2prod( n, v1, v2 ) ) )

	count = count + 1

if count != int( t[ 0 ] ):
	sys.stderr.write( "did not process correct number of cases!\n" )
	sys.exit( 1 )

