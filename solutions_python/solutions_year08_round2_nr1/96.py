#!/usr/bin/python

import sys
import sets

def crd( n, A, B, C, D, x0, y0, M ):
	c = sets.Set()
	X = x0
	Y = y0
	c.add( ( X, Y ) )
	for i in range( 1, n ):
		X = ( A * X + B ) % M
		Y = ( C * Y + D ) % M
		c.add( ( X, Y ) )
	z = []
	z.extend( c )
	return z

def center_ok( a, b, c ):
	x = ( a[ 0 ] + b[ 0 ] + c[ 0 ] )
	y = ( a[ 1 ] + b[ 1 ] + c[ 1 ] )

	if x % 3 == 0 and y % 3 == 0:
		return True
	else:
		return False


f = open( sys.argv[ 1 ] )
t = f.readlines()
f.close()

cases = int( t[ 0 ].strip() )
for i in range( 1, len( t ) ):
	z =  [ int( j ) for j in t[ i ].strip().split() ]
	n, A, B, C, D, x0, y0, M = z
	pts = crd( n, A, B, C, D, x0, y0, M )
#	print pts
	count = 0
	for j in range( len( pts ) ):
		if j < len( pts ) - 2:
			for k in range( j, len( pts ) ):
				if j != k:
					for l in range( k + 1, len( pts ) ):	
						if l != k:
							j1 = pts[ j ]
							k1 = pts[ k ]
							l1 = pts[ l ]
#							print j, k, l, j1, k1, l1
							if center_ok( j1, k1, l1 ):
								count += 1
	sys.stdout.write( "Case #%d: %d\n" % ( i, count ) )

