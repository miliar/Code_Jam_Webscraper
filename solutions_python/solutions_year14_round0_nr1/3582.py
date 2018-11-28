def compRows(cards1, cards2):

	matchCount = 0
	lastCard = 0
	for card1 in cards1:

		for card2 in cards2:

			if card1 == card2:

				lastCard = card1
				matchCount += 1

	if matchCount == 1:

		return lastCard
	elif matchCount == 0:

		return -1	# volunteer cheated
	else:

		return 0	# bad magician

fi = open('A-small-attempt0.in')

casesT = fi.readline()
casesResults = []

for i in range(0, int(casesT)):

	# read ans 1
	ans1 = int(fi.readline())
	# read arrangement
	cards1 = []
	for r in range(1, 5):

		line = fi.readline()
		if r == ans1:

			cards1 = line[:-1].split(" ")
	# read ans 2
	ans2 = int(fi.readline())
	# read arrangement
	cards2 = []
	for r in range(1, 5):

		line = fi.readline()
		if r == ans2:

			cards2 = line[:-1].split(" ")

	casesResults.append(compRows(cards1, cards2))

for i in range(len(casesResults)):

	result = casesResults[i]
	if result == 0:

		mesg = "Bad magician!"
	elif result == -1:

		mesg = "Volunteer cheated!"
	else:

		mesg = result
	print "Case #{0}: {1}".format(i + 1, mesg)

fi.close()

