import sys

case=0
cases=int( sys.__stdin__.readline() )
while case < cases:
	case+=1
	
	turnaround = int( sys.__stdin__.readline() )
	( NA, NB ) = map( lambda x: int(x), sys.__stdin__.readline().split( ' ' ) )

	def parseTime( string ):
		( hrs, mins ) = map( lambda x: int(x), string.split( ':' ) )
		return 60 * hrs + mins

	tableA = [ map( parseTime, sys.__stdin__.readline().split(' ') ) for i in range( NA ) ]
	tableB = [ map( parseTime, sys.__stdin__.readline().split(' ') ) for i in range( NB ) ]

	def requiredTrains( stA, stB ):
		timeline =  [ [ train[0], -1 ] for train in stA ]
		timeline += [ [ train[1] + turnaround, 1 ] for train in stB ]
		timeline.sort( key = lambda x: x[0] - 0.1 * ( x[1] ) )

		req = 0
		ready = 0
		for event in timeline:
			ready += event[1]
			if ready < 0:
				req -= ready
				ready = 0
		return req
	
	print "Case #%d: %d %d" % ( case, requiredTrains( tableA, tableB ), requiredTrains( tableB, tableA ) )


