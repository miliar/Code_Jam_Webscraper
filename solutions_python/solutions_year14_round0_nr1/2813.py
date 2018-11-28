#!/usr/bin/env python


# Get the number of test cases, T.
T = int( raw_input() )
# Process each test case.
for i in xrange( 0, T ):
	candidates = []
	# Getting an answer from the volunteer and
	# getting the card layout are done twice.
	for j in range( 0, 2 ):
		# Get the volunteer's first answer and
		# convert it into an index in the 0-3 range.
		index = int( raw_input() ) - 1
		# Get the layout of the cards.
		for k in range( 0, 4 ):
			line = raw_input()
			# Take note only of the cards in the volunteer's chosen row.
			if k == index:
				candidates.append( [ int( x ) for x in line.split() ] )
	# To determine the volunteer's chosen card, check the candidates lists
	# for any card that appears in both lists.
	chosen = []
	for card in candidates[ 0 ]:
		if card in candidates[ 1 ]:
			chosen.append( card )
	# Provide the verdict on the chosen card.
	if len( chosen ) == 1:
		print "Case #%d: %d" % ( i + 1, chosen[ 0 ] )
	elif len( chosen ) > 1:
		print "Case #%d: Bad magician!" % ( i + 1 )
	else:
		print "Case #%d: Volunteer cheated!" % ( i + 1 )

