#!/usr/bin/python

def readline( f ):
	line = f.readline();
	line = line[:-1]
	return line

def read_integer( f ):
	line = readline( f )
	return int( line )

def read_integer_list( f ):
	line = readline( f )
	integers = line.split( " " )

	for i in range( len( integers ) ):
		integers[i] = int( integers[i] )

	return integers

def print_test_case( i, value ):
	if i <= 0:
		print( "NO VALID VALUE FOR VARIABLE I" )
	else:
		print( "Case #" + str( i ) + ": " + str( value ) )

def binomialCoefficient(n, k):
	if k < 0 or k > n:
		return 0
	if k > n - k: # take advantage of symmetry
		k = n - k
	c = 1
	for i in range(1,k+1):
		c = c * (n - (k - i))
		c = c // i
	return c

def get_left_padding( p ):
	return p + 1

def get_right_padding( p, n, l ):
	return l - p - n + 1

def get_possibilities( ps, pt, l ):
	return get_left_padding( ps ) * get_right_padding( ps, pt - ps + 1, l )

def simplify_name( name ):
	simple = []

	for c in name:
		if c in ['a', 'e', 'i', 'o', 'u']:
			simple.append( False )
		else:
			simple.append( True )

	return simple

f = open( "A-small.in" )

test_cases = read_integer( f )

for tc in range( test_cases ):
	bounds = readline( f ).split( " " )

	name = bounds[0]
	name = simplify_name( name )

	n = int( bounds[1] )

	positions = []
	for i in range( len( name ) ):
		match = True
		for j in range( n ):
			if i + j >= len( name ) or name[i + j] == False:
				match = False
				break

		if match:
			positions.append( i )

	positions.sort()

	possibilities = 0
	for pi in range( len( positions ) ):	
		p = positions[pi]

		limit_left = 0
		if pi > 0:
			limit_left = positions[pi - 1] + 1

		left = p - limit_left + 1
		right = len( name ) - ( p + n ) + 1

		possibilities += left * right

	print_test_case( tc + 1, possibilities )