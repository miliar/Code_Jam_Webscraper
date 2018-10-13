f = open('A-small-attempt0.in', 'r')
numCases = int(f.readline())
x = 1
while x <= numCases:
	possibleCards = []
	firstAnswer = int(f.readline())
	rowNumber = 1
	while rowNumber <= 4:
		row = f.readline()
		if rowNumber is firstAnswer:
			possibleCards = row.split()
			possibleCards = [int(card) for card in possibleCards]
		rowNumber += 1
	secondAnswer = int(f.readline())
	rowNumber = 1
	while rowNumber <= 4:
		row = f.readline()
		if rowNumber is secondAnswer:
			secondPossibleCards = row.split()
			secondPossibleCards = [int(card) for card in secondPossibleCards]
		rowNumber += 1
	actualCards = []
	for card in possibleCards:
		if card in secondPossibleCards:
			actualCards.append(card)
	if len(actualCards) == 0:
		print 'Case #' + str(x) + ': Volunteer cheated!'
	elif len(actualCards) > 1:
		print 'Case #' + str(x) + ': Bad Magician!'
	else:
		print 'Case #' + str(x) + ': ' + str(actualCards[0])
	x += 1