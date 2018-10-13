##
#
#	Replace abc^12 cde^34 with abc^12^ cde^34^
#	^ - mean superscript for PeriodicTable app
#

import sys


if len(sys.argv) != 2:
	sys.exit("Please specify test input file")
inputFilePath = sys.argv[1]
inputFile = open(inputFilePath, 'r')

numberOfTestCases = -1
boards = []
board = []

lineNumber = 0
for line in inputFile.readlines():
	if 0 == lineNumber:
		numberOfTestCases = int(line)
	elif len(line) < 4:
		boards.append(board)
		board = []
	else:
		board.append(line.rstrip('\n'))
	lineNumber += 1

inputFile.close()

######################################

def makeNewBoard(board, symbol):
	result = []
	for line in board:
		newLine = []
		for ch in line:
			if 'T' == ch:
				newLine.append(symbol)
			else:
				newLine.append(ch)
		result.append(newLine)
	return result

def notEnded(board):
	for line in board:
		if '.' in line:
			return True
	return False


def checkBoardForSymbol(board, symbol):
	newBoard = makeNewBoard(board, symbol)
	result = False
	
	for line in newBoard:
		if line == [symbol,symbol,symbol,symbol]:
			result = True
	
	if not result:
		for j in range(0, 4):
			result = True
			for i in range(0, 4):
				if newBoard[i][j] != symbol:
					result = False
					break
			if result:
				break

	if not result:
		result = True
		i = 0
		for j in range(0, 4):
			if newBoard[i][j] != symbol:
				result = False
				break
			i += 1

	if not result:
		result = True
		i = 3
		for j in range(0, 4):
			if newBoard[i][j] != symbol:
				result = False
				break
			i -= 1

	return result


def checkBoard(board):
	if checkBoardForSymbol(board, 'X'):
		return "X won"
	if checkBoardForSymbol(board, 'O'):
		return "O won"
	if notEnded(board):
		return "Game has not completed"

	return "Draw"

######################################

number = 1
for board in boards:
	print "Case #" + str(number) + ": " + str(checkBoard(board))
	number += 1
