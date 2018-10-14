T = int(raw_input())

for case in xrange(T):

	row_1 = int(raw_input())

	# Gets the first set of cards.
	for row in xrange(1,5):
		line = raw_input();

		if row_1 == row:
			cards_1 = line.split(" ")

	row_2 = int(raw_input())

	# Gets the first set of cards.
	for row in xrange(1,5):
		line = raw_input();

		if row_2 == row:
			cards_2 = line.split(" ")

	# Has both lines, now we have to see if the cards
	# are in both selected rows.
	good_cards = []

	for card in cards_1:
		if card in cards_2:
			good_cards.append(card)


	if len(good_cards) == 1:
		print "Case #{0}: {1}".format(case + 1, good_cards[0])
	elif len(good_cards) > 1:
		print "Case #{0}: Bad magician!".format(case + 1)
	else:
		print "Case #{0}: Volunteer cheated!".format(case + 1)
