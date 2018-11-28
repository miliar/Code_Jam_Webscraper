import sys

FILENAME = 'B-small-attempt0.in'

def get_input():
	array_n = []
	length = 0
	i = 0
	with open( FILENAME, 'r' ) as f:
		for row in  f:
			if i == 0:
				length = int( row )
			else:
				array_n.append( int( row.rstrip() ) )
			i += 1
	return array_n, length

def solve( number ):

	for i in range( 0, number ):
		numStr = str( number - i )
		if isTidyNumber( numStr ):
			return numStr

def isTidyNumber( numberStr ):
	
	if len( numberStr ) == 1:
		return True	

	for i in range( 0, len( numberStr ) - 1 ):
		if ( int( numberStr[ i ] ) > int( numberStr[ i + 1 ] ) ):
			return False
	
	return True
		
	

if __name__ == '__main__':
	array, count = get_input()

	for i in range( 0, count ):
		print('Case #{i}: {result}'.format( i = str( i + 1), result = solve( array[ i ] ) ) )


