#!/usr/bin/python

from copy import copy, deepcopy

def readline( f ):
	line = f.readline()
	line = line[:-1]
	return line

def read_integer( f ):
	string = readline( f )
	return int( string )

def read_integer_list( f ):
	string = readline( f )
	string_list = string.split( " " )

	for i in range( len( string_list ) ):
		string_list[i] = int( string_list[i] )

	return string_list

def is_reachable( lawn, w, h, xt, yt ):
	# check if it is horizontally reachable
	reachable = True
	for x in range( w ):
		if lawn[x][yt] is None:
			reachable = False

	if reachable:
		return True

	# check if it is horizontally reachable
	reachable = True
	for y in range( h ):
		if lawn[xt][y] is None:
			reachable = False

	return reachable

def is_moweable( lawn, w, h ):
	max_height = 0
	undecided_fields = False

	# determine maximum height and whether some fields are still undecided
	for x in range( w ):
		for y in range( h ):
			curr_height = lawn[x][y]
			if curr_height is not None:
				undecided_fields = True

				if max_height < curr_height:
					max_height = curr_height

	if not undecided_fields:
		# all fields are moweable
		return True

	# determine whether all remaining fields which have the maximum height as their height are
	# moweable
	new_lawn = deepcopy( lawn )
	for x in range( w ):
		for y in range( h ):
			curr_height = new_lawn[x][y]

			if curr_height is not None and curr_height == max_height:
				if is_reachable( lawn, w, h, x, y ):
					new_lawn[x][y] = None
				else:
					# this field is not moweable
					return False

	for l in new_lawn:
		print( l )

	# return whether the remaining lawn is moweable
	return is_moweable( new_lawn, w, h )

f = open( "B-large.in", "r" )
test_cases = read_integer( f )

for i in range( test_cases ):
	dim = read_integer_list( f )
	w = dim[0]
	h = dim[1]

	lawn = []
	for x in range( w ):
		lawn.append( read_integer_list( f ) )

	result = "NO"
	if is_moweable( lawn, w, h ):
		result = "YES"

	print( "Case #" + str( i + 1 ) + ": " + result )