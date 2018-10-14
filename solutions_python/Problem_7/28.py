import sys

case=0
cases=int( sys.__stdin__.readline() )
while case < cases:
	case+=1

	(n, A, B, C, D, x0, y0, M) = map( lambda x: int(x), sys.__stdin__.readline().rstrip().split( ' ' ) )

	x,y = x0,y0
	trees = [ [x,y] ]
	for i in range( 1, n ):
		x = ( A * x + B ) % M
		y = ( C * y + D ) % M
		trees.append( [x,y] )

	variants = 0

	for i in range( n ):
		for j in range( i + 1, n ):
			for k in range( j + 1, n ):
				if ( trees[i][0] + trees[j][0] + trees[k][0] ) % 3 == 0:
					if ( trees[i][1] + trees[j][1] + trees[k][1] ) % 3 == 0:
						variants += 1

	
	print "Case #%d: %d" % ( case, variants )


