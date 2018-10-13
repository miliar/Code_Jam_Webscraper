import math
import sys

def isWin(board):

	for x in GetVectors(board):
		if x.replace("T", "X") == "XXXX":
			return "X"
		if x.replace("T", "O") == "OOOO":
			return "O"
	return ""

def isDraw(board):
	for i in range(0,4):
		if board[i].find(".") != -1:
			return False
	return True

def GetVectors(board):
	result = []
	result.append(board[0])
	result.append(board[1])
	result.append(board[2])
	result.append(board[3])

	for column in range(0,4):
		result.append(board[0][column] + board[1][column] + board[2][column] + board[3][column])

	result.append(board[0][0] + board[1][1] + board[2][2] + board[3][3])
	result.append(board[0][3] + board[1][2] + board[2][1] + board[3][0])

	return result

case = 0

board = ["","","",""]
boardLine = -1

for line in sys.stdin:
	count = 0
	boardLine = boardLine + 1
	if boardLine == 0:
		continue
	if boardLine == 5:
		boardLine = 0
		continue

	board[boardLine-1] = line.strip()
	if boardLine != 4:
		continue
	
	if len(line.strip()) == 0:
		break
	
	case = case + 1

	win = isWin(board)
	if len(win) > 0:
		print "Case #{0}: {1} won".format(case, win)
		continue

	if isDraw(board):
		print "Case #{0}: Draw".format(case)
		continue

	print "Case #{0}: Game has not completed".format(case)

