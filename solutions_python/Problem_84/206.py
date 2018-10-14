#! /usr/bin/python
import sys

T = int( sys.stdin.readline() )


for i in range( T ) :

	line = sys.stdin.readline().split()
	line = [ int(n) for n in line ]
	R = line[0]
	C = line[1]

	data = []
	for j in range( R ) :
		row = sys.stdin.readline()
		row = row[ :-1]
		row = [ s for s in row ]
		data.append( row )
	
	#print "data :",data
	possible = True
	#print "initial data"
	"""
	for j in range( R ) :
		print "".join( data[j] )
	print "done initial"
	"""

	for j in range( R ) :
		if not possible :
			break
		for k in range( C ) :
			#print "check k in col",k
			
			if data[ j ][ k ] == '#' :
				if ( j+1 <= R-1 and k+1 <= C-1  ) and ( ( data[ j ][ k ] == '#' ) and ( data[ j ][ k+1 ] == '#' ) and ( data[ j+1 ][ k ] == '#' ) and ( data[ j+1 ][ k+1 ] == '#' ) ) :
					#print "substtng"
					data[ j ][ k ] = '/'
					data[ j ][ k+1 ] = '\\'
					data[ j+1 ][ k ] = '\\'
					data[ j+1 ][ k+1 ] = '/'
				else :
					#print "possible false in k = ",k
					possible = False	
					break
			else :
				pass
	if not possible :
		print "Case #%d: \n%s"%((i+1),"Impossible"  )
		continue
				
	print "Case #%d:"%((i+1), )
	for j in range( R ) :
		print "".join( data[j] )
