#Tic Tac Toe
def checkHorizontal(grid):
	for row in grid:
		numX = 0
		numY = 0
		for letter in row:
			if letter == "X":
				numX += 1
			elif letter == 'O':
				numY += 1
			elif letter == 'T':
				numX += 1
				numY += 1
		if numX == 4:
			return 'X won'
		elif numY == 4:
			return 'O won'
	return 'Draw'

def checkVertical(grid):
	for i in range(4):
		numX = 0
		numY = 0
		for j in range(4):
			if grid[j][i] == 'X':
				numX += 1
			elif grid[j][i] == 'O':
				numY += 1
			elif grid[j][i] == 'T':
				numX += 1
				numY += 1
		if numX == 4:
			return "X won"
		elif numY == 4:
			return "O won"
	return "Draw"

def checkDiagonal(grid):
	numX = 0
	numY = 0
	ind = 0
	for row in grid:
		if row[ind] == 'X':
			numX += 1
		elif row[ind] == 'O':
			numY += 1
		elif row[ind] == 'T':
			numX += 1
			numY += 1
		ind += 1
	if numX == 4:
		return 'X won'
	elif numY == 4:
		return 'O won'
	else:
		return 'Draw'

def checkDiagonal2(grid):
	numX = 0
	numY = 0
	ind = 3
	for row in grid:
		if row[ind] == 'X':
			numX += 1
		elif row[ind] == 'O':
			numY += 1
		elif row[ind] == 'T':
			numX += 1
			numY += 1
		ind -= 1
	if numX == 4:
		return 'X won'
	elif numY == 4:
		return 'O won'
	else:
		return 'Draw'

def checkIfGameFinished(grid):
	valid = ['X', 'O', 'T']
	for row in grid:
		for letter in row:
			if letter not in valid:
				return False
	return True

def ticTacToe():
	gameResults = [0] * 1000
	for i in range(int(numGrids)):
		gameIsFinished = False
		grid = []
		for j in range(4):
			grid.append(f.readline().strip('\n'))
		print(grid)
		result = checkHorizontal(grid)
		if result == 'X won' or result == 'O won' and not gameIsFinished:
			gameResults[i] = result
			gameIsFinished = True
		result = checkVertical(grid)
		if result == 'X won' or result == 'O won' and not gameIsFinished:
			gameResults[i] = result
			gameIsFinished = True
		result = checkDiagonal(grid)
		if result == 'X won' or result == 'O won' and not gameIsFinished:
			gameResults[i] = result
			gameIsFinished = True
		result = checkDiagonal2(grid)
		if result == 'X won' or result == 'O won' and not gameIsFinished:
			gameResults[i] = result
			gameIsFinished = True

		if not gameIsFinished:
			if checkIfGameFinished(grid):
				gameResults[i] = "Draw"
			else:
				gameResults[i] = "Game has not completed"
		gameResults[i] = "Case #" + str(i+ 1) + ": " +  gameResults[i]
		print(gameResults[i])
		f.readline()
	return gameResults


f = open("A-large.in", "r+")
numGrids = f.readline()
p = open("Out.out", "w+")

output = ticTacToe()
for line in output:
	print(line)
	p.write(line + "\n")