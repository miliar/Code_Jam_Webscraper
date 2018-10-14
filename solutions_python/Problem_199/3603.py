# coding: UTF-8

import sys

MAX_STR_LEN = 10
HAPPY_SIDE = '+'
NOTHING_SIDE = '-'
FILENAME = 'A-small-attempt1.in'

def solve( pancakes, flipper_size ):
	tmpPancakes = pancakes
	
	count = 0

	for i in range( 0, len ( pancakes ) ):
		if isAllHappy( tmpPancakes ):
			return count

		if tmpPancakes[ i ] == NOTHING_SIDE:
			if ( i + flipper_size ) > len( pancakes ):
				return -1
			
			tmpPancakes = flip( tmpPancakes, flipper_size, i )
			count += 1

		
def isAllHappy( pancakes ):
	for p in pancakes:
		if p == NOTHING_SIDE:
			return False
	
	return True

	
def flip( pancakes, flipper_size, left_iter ):

	flipped_pancakes = pancakes[ left_iter : ( left_iter + flipper_size) ]
	
	
	new_pancakes = ''
	for i in range( flipper_size ):
		if flipped_pancakes[ i ] == HAPPY_SIDE:
			new_pancakes += NOTHING_SIDE
		else:
			new_pancakes += HAPPY_SIDE
	right_side = ( left_iter + flipper_size )

	result_pancakes = ''
	if left_iter > 0:
		result_pancakes = pancakes[ 0 : left_iter ]

	result_pancakes += new_pancakes
	

	if len( pancakes ) >= right_side:
		result_pancakes +=  pancakes[ right_side : ]
	
	return result_pancakes

	
def get_input():
	array_p = []
	array_f = []
	length = 0
	i = 0
	with open( FILENAME, 'r' ) as f:
		for row in  f:
			if i == 0:
				length = int( row )
			else:
				splits = row.split( ' ' )
				array_p.append( splits[ 0 ] )
				array_f.append( int( splits[ 1 ].rstrip() ) )
			i += 1
	return array_p, array_f, length


if __name__ == '__main__':
	pancakes, flippers, length = get_input()
	
	for i in range( 0, length ):
		result = solve( pancakes[ i ], flippers[ i ] )
		if result == -1 :
			result = 'IMPOSSIBLE'
		print( 'Case #{i}: {result}'.format( i = str( i + 1 ), result = str( result ) ) )
