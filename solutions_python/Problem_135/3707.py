import sys

class TestCase():
	def __init__(self):
		self.firstGuess = None
		self.secondGuess = None
		self.firstCards = []
		self.secondCards = []
	
	def solve(self):
		firstLine = self.firstCards[self.firstGuess-1]
		secondLine = self.secondCards[self.secondGuess-1]
		matches = []
		for card in secondLine:
			if card in firstLine:
				matches.append(card)

		if len(matches) == 0:
			return "Volunteer cheated!"
		elif len(matches) > 1:
			return "Bad magician!"
		else:
			return matches[0]



if len(sys.argv) < 2:
	print "Need input text!"
	sys.exit(1)

with open(sys.argv[1], "r") as f:

	rows = f.readlines()

	splitRows = []
	testCases = []
	currentGuessedRow = 0
	numTestCases = 0

	for i in range(len(rows)):
		line = rows[i].rstrip("\n").split(" ")
		if i == 0:
			numTestCases = int(line[0])
		elif i % 10 == 1:
			testCases.append(TestCase())
			testCases[-1].firstGuess =  int(line[0])
		elif i % 5 == 1:
			testCases[-1].secondGuess =  int(line[0])
		else:
			if not testCases[-1].secondGuess:
				testCases[-1].firstCards.append([int(item) for item in line])
			else:
				testCases[-1].secondCards.append([int(item) for item in line])

	for case, test in enumerate(testCases):
		print "Case #" + str(case + 1) + ": " + str(test.solve())





