#Tidy Numbers
import sys

digits = '0123456789'

def getInput( fp ):
	with open( fp, 'r' ) as f:
		input = [l.rstrip() for l in f]
	return input
	

def isTidy( num_string ):
	is_tidy = True
	for i in range( 1, len( num_string ) ):
		if int( num_string[i] ) < int( num_string[i-1] ):
			is_tidy = False
			
	return is_tidy
	
def removeLeadingZeros( string ):
	length = len( string )
	non_zero = False
	for index in range( length ):
		if string[index] != '0':
			return string[index:]
			
	
def getLowerDigit( i ):
	index = digits.index( i )
	index -= 1
	if index < 0:
		index = len( digits ) - 1
	return digits[index]

def lastTidyNumber( N ):
	# Consider the chars of the number in order, until you find the first untidy pair. Then decrease the first char by 1, and change all remaining chars to 9
	string = str( N )
	length = len( string )
	if isTidy( string ):
		return string
	for i in range( length ):
		if not isTidy( string[i] + string[i+1] ):
			string = string[:i] + getLowerDigit( string[i] )
			for a in range( i + 2, length + 1 ):
				string = string + '9'
			break
	string = removeLeadingZeros( string )
	if not isTidy( string ):
		return lastTidyNumber( string )
	return string
		
		
in_fp = r"C:\Users\tristan.sebens\Downloads\B-large.in"
out_fp = r"C:\Users\tristan.sebens\Documents\Code\Google Code Jam\2017\Qualifying Round\out.txt"
input = getInput( in_fp )[1:]
with open( out_fp, 'w' ) as out:
	case = 1
	for i in input:
		ltn = lastTidyNumber( i )
		out.write( "Case #%s: %s\n" % ( case, ltn ) )
		case += 1

