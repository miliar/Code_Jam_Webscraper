
def checkRow(linesLst, _gameState):
	Xwon = 1
	Owon = 2
	Draw = 3
	notCompleted = 4
	none = 5

	gameState = _gameState
	
	for line in linesLst:
		lineState = line[0]
		startNum = 1
		if lineState == 'T':
			lineState = line[1]
			startNum = 2
		#print 'lineState', lineState, 'startNum', startNum, 'line', line
		if lineState == '.':
			gameState = notCompleted
			continue
		for i in range(startNum, len(line)):
			#print 'i', i, 'line[i]', line[i]
			if line[i] == '.':
				gameState = notCompleted
				break
			if line[i] != lineState and line[i] != 'T':
				#print 'draw!'
				if gameState != notCompleted:
					gameState = Draw
				break
			if i == len(line) - 1 and lineState == 'X':
				#print 'lineStateX!', gameState
				gameState = Xwon
				return gameState
			elif i == len(line) - 1 and lineState == 'O':
				#print 'lineStateO!', gameState
				gameState = Owon
				return gameState
	return gameState

def checkColumn(linesLst, _gameState):
	Xwon = 1
	Owon = 2
	Draw = 3
	notCompleted = 4
	none = 5

	gameState = _gameState
	
	for i in range(4):
		lineState = linesLst[0][i]
		startNum = 1
		if lineState == 'T':
			lineState = linesLst[1][i]
			startNum = 2
		if lineState == '.':
			gameState = notCompleted
			continue
		for j in range(startNum, 4):
			if linesLst[j][i] == '.':
				gameState = notCompleted
				break
			if linesLst[j][i] != lineState and linesLst[j][i] != 'T':
				if gameState != notCompleted:
					gameState = Draw
				break
			if  j == 3 and lineState == 'X':
				gameState = Xwon
				return gameState
			elif j == 3 and lineState == 'O':
				gameState = Owon
				return gameState
	return gameState

def checkDiagonal1(linesLst, _gameState):
	Xwon = 1
	Owon = 2
	Draw = 3
	notCompleted = 4
	none = 5

	gameState = _gameState
	
	lineState = linesLst[0][0]
	startNum = 1
	if lineState == 'T':
		lineState = linesLst[1][1]
		startNum = 2
	if lineState == '.':
		gameState = notCompleted
		return gameState
	for i in range(startNum, 4):
		if linesLst[i][i] == '.':
			gameState = notCompleted
			return gameState
		if linesLst[i][i] != lineState and linesLst[i][i] != 'T':
			if gameState != notCompleted:
				gameState = Draw
			return gameState
	if lineState == 'X':
		gameState = Xwon
		return gameState
	elif lineState == 'O':
		gameState = Owon
		return Owon
	return gameState

def checkDiagonal2(linesLst, _gameState):
	Xwon = 1
	Owon = 2
	Draw = 3
	notCompleted = 4
	none = 5

	gameState = _gameState

	lineState = linesLst[0][3]
	startNum = 1
	if lineState == 'T':
		lineState = linesLst[1][2]
		startNum = 2
	if lineState == '.':
		gameState = notCompleted
		return gameState
	for i in range(startNum, 4):
		if linesLst[i][3 - i] == '.':
			gameState = notCompleted
			return gameState
		if linesLst[i][3 - i] != lineState and linesLst[i][3 - i] != 'T':
			if gameState != notCompleted:
				gameState = Draw
			return gameState
	if lineState == 'X':
		gameState = Xwon
		return gameState
	elif lineState == 'O':
		gameState = Owon
		return Owon
	return gameState

Xwon = 1
Owon = 2
Draw = 3
notCompleted = 4
none = 5
gameState = none
#f = open('sample.txt', 'r')
f = open ('A-small-attempt3.in', 'r')
#f = open('A-large-practice.in', 'r')
f2 = open('output.txt', 'a')

inputData = []
inputNumber = 1
lineNumber = 1
firstFlg = 1

for line in f:
	line = line.strip()
	#print 'line', line
	#print 'len(line)', len(line)
	if len(line) == 0:
		lineNumber = 1
		continue
	if firstFlg == 1:
		numOfInput = line[0]
		#print 'numOfInput:', numOfInput
		firstFlg = 0
	else:
		if lineNumber == 1:
			line1 = line
			lineNumber = lineNumber + 1
			#print 'line1', line1
		elif lineNumber == 2:
			line2 = line
			#print 'line2', line2
			lineNumber = lineNumber + 1
		elif lineNumber == 3:
			line3 = line
			#print 'line3', line3
			lineNumber = lineNumber + 1
		elif lineNumber == 4:
			line4 = line
			#print 'line4', line4
			linesLst = [line1, line2, line3, line4]
			gameState = checkRow(linesLst, gameState)
			#print 'gameState', gameState
			if gameState != Xwon and gameState != Owon: 
				gameState = checkColumn(linesLst, gameState)
				#print 'gameState', gameState
			if gameState != Xwon and gameState != Owon:
				gameState = checkDiagonal1(linesLst, gameState)
			if gameState != Xwon and gameState != Owon:
				gameState = checkDiagonal2(linesLst, gameState)

			if gameState == Xwon:
				result = "X won"
			elif gameState == Owon:
				result = "O won"
			elif gameState == Draw:
				result = "Draw"
			elif gameState == notCompleted:
				result = "Game has not completed"

			#print 'Case #' + str(inputNumber) + ': ' + result
			f2.write('Case #' + str(inputNumber) + ': ' + result + '\n')
			inputNumber = inputNumber + 1
			if inputNumber > numOfInput:
				break
			gameState = none

f2.close()
f.close()
	
