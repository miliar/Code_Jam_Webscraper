import os, sys, sets

T = int( raw_input().rstrip() )

for t in xrange(T):

	first_matrix = [[0 for x in xrange(4)] for x in xrange(4)]

	first_choice 	= int( raw_input().rstrip() ) - 1

	for i in xrange(4):
		line = raw_input().rstrip().split(' ')
		for j in xrange(4):
			first_matrix[i][j] = int( line[j] )

	first_set 			= set( first_matrix[ first_choice ] )

	second_matrix 	= [[0 for x in xrange(4)] for x in xrange(4)]

	second_choice 	= int( raw_input().rstrip() ) - 1

	for i in xrange(4):
		line = raw_input().rstrip().split(' ')
		for j in xrange(4):
			second_matrix[i][j] = int( line[j] )

	second_set			= set( second_matrix[ second_choice ] )

	intersection 		= first_set & second_set

	if 		len(intersection) == 0:
		print "Case #%s: Volunteer cheated!" % ( t+1 ) 
	elif 	len(intersection) == 1:
		print "Case #%s: %s" % ( t+1, list(intersection)[0] )
	else:
		print "Case #%s: Bad magician!" % ( t+1 )
