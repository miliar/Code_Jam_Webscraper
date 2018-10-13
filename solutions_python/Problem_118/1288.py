import math

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

	A = int( dimensions[0] )
	B = int( dimensions[1] )

	in_cases.append( (A, B) )


def isPalindrome( number ) :
	number = str( int( number ) )
	length = len( number )

	palindrome = True
	for i in range( length / 2 ) :
		if number[i] != number[length-1] :
			palindrome = False
			break
	return palindrome


def isqrt( x ) :
	res = 0

	# "one" starts at the highest power of four <= than the argument.
	one = 1
	while True :
		next = one << 2
		if next > x :
			break
		one = next

	while one != 0 :
		if x >= res + one :
			x -= res + one
			res += one << 1

		res = res >> 1
		one = one >> 2

	return res


def clacState( case ) :
	a = case[0]
	b = case[1]
	low = isqrt( case[0] ) - 1
	high = isqrt( case[1] ) + 1

	n = low
	count = 0
	while n < high :
		square = n*n
		if not (square < a or square > b) :
			if isPalindrome( n ) and isPalindrome( square ) :
				count += 1
		n += 1

	return str( count )


for i in range( len( in_cases ) ) :
	case = in_cases[i]
	state = clacState( case )
	print >>out_file, 'Case #' + str(i+1) + ': ' + state
	#print >>out_file, 'Case #' + str(i+1) + ': ' + state
