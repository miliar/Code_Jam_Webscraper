import string 

def findStatusOfGame(board):
	#print 'board' + str(board)
	verticalChoices = zip(board[0], board[1], board[2], board[3])
	verticalChoices = [list(elem) for elem in verticalChoices]
	diagonals = [[board[0][0], board[1][1], board[2][2], board[3][3]], [board[0][3], board[1][2], board[2][1], board[3][0]]]
	choices = board + verticalChoices + diagonals
	#print choices
	checkChoices = [list(set(elem)) for elem in choices]
	#print checkChoices
	if ['X', 'T'] in checkChoices or ['X'] in checkChoices or ['T', 'X'] in checkChoices:
		return 'X won'
	if ['O', 'T'] in checkChoices or ['O'] in checkChoices or ['T', 'O'] in checkChoices:
		return 'O won'
	for elem in checkChoices:
		if '.' in elem:
			return 'Game has not completed'
	return 'Draw'

outputList = []
with open('A-large.in') as f:
	listFile = f.readlines()
	noOfCases = int(listFile[0])
	for i in range(1, noOfCases + 1):
		index = (i-1)*5 + 1
		#print "lenOfVec : " + str(lenOfVec)
		#print [int(elem) for elem in listFile[index + 2].split()]
		result = ''
		board = []
		for j in range(index, index + 4):
			board.append(list(listFile[j])[:-1])
		result = findStatusOfGame(board)
		outputList.append([i, result])
outputFile = open('outputlarge', 'w')
for elem in outputList:
	outputFile.write('Case #' + str(elem[0]) + ": " + elem[1] + "\n")
