import sys

debugging = False

def debug( string ):
	if debugging:
		print( string )


def solve( p ):
	sum = 0
	i = 0
	needed = 0
	
	debug( '\n\nSolving %s' % p )
	
	for num in p:
		debug( 'People who need %d clappers: %d' % ( i, int(num) ) )
		if ( sum + needed < i ) and num != '0':
			needed += i - ( sum + needed )
			debug( 'Not sufficient, %d needed' % (i-(sum+needed)) )
		else:
			debug( 'Sufficient' )
		i += 1
		sum += int( num )
		
	return needed

with open( 'A-large.in' ) as file:
	lines = file.read().split( '\n' )

	count = int( lines[ 0 ] ) #testcase count
	testcases = lines[ 1: ]
	tc = 0

	for testcase in testcases:
		tc += 1 # Testcase number
		
		input = testcase.split( ' ' )

		problem = input[ 1 ]

		solution = solve( problem )
		
		print( 'Case #%d: %d' % ( tc, solution ) )