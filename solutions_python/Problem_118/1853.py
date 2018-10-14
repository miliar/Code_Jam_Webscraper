import math

def isok( num ):
	if str( num ) != str( num )[::-1]:
		return False
	root = int( math.sqrt( num ) ) 

	if root ** 2 != num:
		return False

	if str( root ) != str( root )[::-1]:
		return False

	return  True


tn = int ( raw_input().strip() )

for cc in xrange( 1, tn+ 1 ):
	A, B = map( int, raw_input().strip().split() )
	print "Case #%d:" % cc, len( [ i for i in xrange(A,B+1) if isok( i )  ] )
