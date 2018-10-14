#! /usr/bin/python
import sys

N = int( sys.stdin.readline() )


for i in range( N ) :

	line = sys.stdin.readline().split()

	buttons = int( line[0] )

	line = line[ 1: ]


	pos_o = 1
	pos_b = 1
	time = 0 
	time_prev_o = 0
	time_prev_b = 0
	for j in  range( buttons ) :
		if line[ 2*j ]  == 'O' :
			new = int( line[ 2*j+1 ]  )
			shift = abs( new - pos_o )
			if time_prev_o < time :
				time = max( time_prev_o + shift , time )
				time += 1
				pos_o = new
				time_prev_o = time

			else :
				time += shift
				time += 1
				pos_o = new
				time_prev_o = time

		elif line[ 2*j ]  == 'B' :
			new = int( line[ 2*j+1 ]  )
			shift = abs( new - pos_b )

			if time_prev_b < time :
				time = max( time_prev_b + shift , time )
				time += 1
				pos_b = new
				time_prev_b = time

			else :
				time += shift
				time += 1
				pos_b = new
				time_prev_b = time
			

	print "Case #%d: %d"%((i+1),time )
