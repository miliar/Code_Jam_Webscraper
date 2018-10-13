
def checkForWin(row):
	print row
	xCount = 0
	yCount = 0
	hasT = False
	blankSpaces = 0
	for ch in list(row):
		if ch == 'X':
			xCount += 1
		if ch == 'O':
			yCount += 1
		if ch == '.':
			blankSpaces += 1
		if ch == 'T':
			hasT = True
	if (xCount == 4) or (xCount == 3 and hasT):
		return 1
	if (yCount == 4) or (yCount == 3 and hasT):
		return 2
	if blankSpaces > 0:
		return -1
	return 0




def getGameState(ticTacTomekBoard):
	"""
	First check
	"""
	hasBlankSpaces = False
	for x in range(4):
		#Check the columns
		result = checkForWin(ticTacTomekBoard[x][0] + ticTacTomekBoard[x][1] + ticTacTomekBoard[x][2] + ticTacTomekBoard[x][3])
		if result == 1:
			return "X won"
		if result == 2:
			return "O won"
		if result == -1:
			hasBlankSpaces = True

		#Check the rows
		result = checkForWin(ticTacTomekBoard[0][x] + ticTacTomekBoard[1][x] + ticTacTomekBoard[2][x] + ticTacTomekBoard[3][x])
		if result == 1:
			return "X won"
		if result == 2:
			return "O won"

	#check the diagonal cases
		result = checkForWin(ticTacTomekBoard[0][0] + ticTacTomekBoard[1][1] + ticTacTomekBoard[2][2] + ticTacTomekBoard[3][3])
		if result == 1:
			return "X won"
		if result == 2:
			return "O won"

		result = checkForWin(ticTacTomekBoard[0][3] + ticTacTomekBoard[1][2] + ticTacTomekBoard[2][1] + ticTacTomekBoard[3][0])
		if result == 1:
			return "X won"
		if result == 2:
			return "O won"

	#If here, the game is either not complete or a draw
	if hasBlankSpaces:
		return "Game has not completed"
	else:
		return "Draw"

def readInputFile(fileName):
	out = open('ouput.txt', 'w+')
	inp = open(fileName, 'r')
	#first is number of cases
	cases = inp.readline()
	for i in range(int(cases)):
		board = []

		line = list(inp.readline())
		board.append(line)
		line = list(inp.readline())
		board.append(line)
		line = list(inp.readline())
		board.append(line)
		line = list(inp.readline())
		board.append(line)
		#should have a board
		i += 1
		print "Case " + str(i)
		out.write("Case #{0}: {1}\n".format(i, getGameState(board)))
		inp.readline()

readInputFile('A-large.in')