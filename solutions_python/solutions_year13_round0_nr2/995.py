from collections import *

in_file = open( 'input.txt' )
out_file = open( 'output.txt', 'w' )
input_lines = in_file.readlines( )

in_line_index = 0
num_in_cases = int( input_lines[in_line_index] )

in_line_index += 1 ;

in_cases = []

for i in range( num_in_cases ) :
	in_case = []

	dimensions = input_lines[in_line_index].split( )
	in_line_index += 1 ;

	N = int( dimensions[0] )
	M = int( dimensions[1] )

	for i in range( N ) :
		line = [ int( x ) for x in input_lines[in_line_index][:-1].split( ) ]
		in_case.append( line )
		in_line_index += 1 ;
	in_cases.append( in_case )


def eliminateRows( case, rows, cols, height ) :
	for line_index in list( rows ) :
		line = case[line_index]
		covered = True
		for square_index in cols :
			square = line[square_index]
			if square > height :
				covered = False
				break
		if covered :
			rows.remove( line_index )

def eliminateCols( case, rows, cols, height ) :
	transposed = zip( *case )
	eliminateRows( transposed, cols, rows, height )

def isReachable( case, rows, cols, height ) :
	eliminateRows( case, rows, cols, height )
	eliminateCols( case, rows, cols, height )

	for line_index in rows :
		line = case[line_index]
		for square_index in cols :
			square = line[square_index]
			if square <= height :
				return False

	return True


def clacState( case ) :
	heights = OrderedDict.fromkeys( [height for line in case for height in line] ).keys( )
	heights.sort( )

	rows = set( [ i for i in range( len( case ) ) ] )
	cols = set( [ i for i in range( len( case[0] ) ) ] )

	possible = True
	for height in heights :
		if not isReachable( case, rows, cols, height ) :
			possible = False
			break

	return 'YES' if possible else 'NO'


for i in range( len( in_cases ) ) :
	case = in_cases[i]
	state = clacState( case )
	print >>out_file, 'Case #' + str(i+1) + ': ' + state
	#print >>out_file, 'Case #' + str(i+1) + ': ' + state
