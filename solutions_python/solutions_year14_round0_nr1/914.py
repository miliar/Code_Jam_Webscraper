import sys

def intersection( list1, list2 ):
	result = [ x for x in list1 for y in list2 if x == y ]
	return result

fin = open("input.txt", "r" )
fout = open("output.txt", "w" )

testcases = int( fin.readline().split()[0] )

for test_id in range( testcases ):

	a, b = [], []

	x = int( fin.readline().split()[0] ) - 1

	for i in range( 4 ):
		a.append( [ int(x) for x in fin.readline().split(' ') ] )

	y = int( fin.readline().split()[0] ) - 1

	for i in range( 4 ):
		b.append( [ int(x) for x in fin.readline().split(' ') ] )

	c = intersection( a[x], b[y] )

	fout.write( "Case #%d: " % ( test_id + 1 ) )

	if len( c ) == 0:
		fout.write( "Volunteer cheated!\n" )
	elif len( c ) == 1:
		fout.write( "%d\n" % c[ 0 ] )
	else:
		fout.write( "Bad magician!\n" )