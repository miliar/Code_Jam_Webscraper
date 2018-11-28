
def checkHorizontal(board):
	for player in ['X', 'O']:
		for row in range(4):
			won = True
			for col in range(4):
				if board[row][col] != player and board[row][col] != 'T':
					won = False
			if won:
				return player
	return '.'

def checkVertical(board):
	for player in ['X', 'O']:
		for col in range(4):
			won = True
			for row in range(4):
				if board[row][col] != player and board[row][col] != 'T':
					won = False
			if won:
				return player
	return '.'

def checkDiagonals(board):
	for player in ['X', 'O']:
		won = True
		for col in range(4):
			if board[col][col] != player and board[col][col] != 'T':
				won = False
		if won:
			return player
		
		won = True
		for col in range(4):
			if board[3-col][col] != player and board[3-col][col] != 'T':
				won = False
		if won:
			return player
		
	return '.'

def checkForWin(board):
	result = checkHorizontal(board)
	if result == '.':
		result = checkVertical(board)
	if result == '.':
		result = checkDiagonals(board)
	return result

def checkDraw(board):
	for i in range(4):
		for j in range(4):
			if board[i][j] == '.':
				return '.'
	return 'D'

def readBoard():
	board = []
	for i in range(4):
		board += [input()]
	input()
	return board

#read in stuff
nCases = int(input())
case = 0
while case < nCases:
	case += 1
	board = readBoard()
	result = checkForWin(board)
	if result == '.':
		result = checkDraw(board)
	text = "Case #{0}: {1}"
	if result == '.':
		text = text.format(case, "Game has not completed")
	elif result == 'D':
		text = text.format(case, "Draw")
	else:
		text = text.format(case, "{0} won".format(result))
	print(text)