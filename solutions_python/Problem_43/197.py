import sys, math

total_count = int( sys.stdin.readline() )

for linenum in range( total_count ):
	string = sys.stdin.readline().strip( '\r\n' )

	charset = set()

	for char in string:
		charset.add( char )

	base = len( charset )
	value = 0

	print( 'Case #%d:' % ( linenum + 1 ), end = '' )

	if base == 1 and len( string ) > 1:
		base = 2

	if len( string ) == 1:
		value = 1
	else:
		strdict = {}

		value = 0
		counter = 0

		for index in range( len( string ) ):
			char = string[ index ]

			if char not in strdict:
				if index == 0:
					strdict[ char ] = 1
				else:
					if counter == 1:
						strdict[ char ] = 0
					else:
						strdict[ char ] = counter

				counter += 1

			value += strdict[ char ] * ( base ** ( len( string ) - ( index + 1 ) ) )

	print( ' %d' % ( value ) )
