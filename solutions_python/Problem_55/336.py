import sys

def calSum( newPos ):
	oneRoundSum = 0
	oneRoundCount = 0
	partialSum = []
	start = 0
	newPos = [ i for i in  newPos ]
	#print newPos
	while True:
		if type( newPos[ start ] ) is int:
			break
		partialSum += [ oneRoundSum ]
		oneRoundSum += newPos[ start ][ 1 ]
		oneRoundCount += 1

		tmp = start
		start = newPos[ start ][ 0 ]
		newPos[ tmp ] = oneRoundCount - 1

	#print start, newPos[ start ], oneRoundSum, oneRoundCount, partialSum
	return start, newPos[ start ], oneRoundSum, oneRoundCount, partialSum

cc = int( sys.stdin.readline() )

for i in range( cc ):
	R, quota, N = map( int, sys.stdin.readline().split() )
	numbers = map( int, sys.stdin.readline().split() )
	newPos = [ 0 ] * N
	for j in range( N ):
		total = 0
		k = j
		while total + numbers[ k % N ] <= quota and k - j < N:
			total += numbers[ k % N ]
			k += 1
		newPos[ j ] = ( k%N, total )

	pos, start, oneRoundSum, oneRoundCount, partialSum = calSum( newPos )
	if R < len( partialSum ):
		print "Case #%d: %d" % ( i+1, partialSum[ R % oneRoundCount ] )
	else:
		R -= start
		pos1, start1, oneRoundSum1, oneRoundCount1, partialSum1 = calSum( map( lambda x: ( x[0] - pos, x[1] ), newPos[pos:] + newPos[:pos] ) )
		print "Case #%d: %d" % ( i+1, partialSum[ start ] + oneRoundSum1 * ( R / oneRoundCount1 ) + partialSum1[ R % oneRoundCount1 ] )
