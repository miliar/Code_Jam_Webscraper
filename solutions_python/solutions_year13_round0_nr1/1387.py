import sys

f = open(sys.argv[1])
T = int(f.readline())

def checkWin(board, pl):
	for i in xrange(4):
		for j in xrange(4):
			if board[i][j] not in pl:
				break
		else:
			return True
		for j in xrange(4):
			if board[j][i] not in pl:
				break
		else:
			return True
	for i in xrange(4):
		if board[i][i] not in pl:
			break
	else:
		return True
	for i in xrange(4):
		if board[i][3-i] not in pl:
			break
	else:
		return True
	return False

def checkFree(board):
	for i in xrange(4):
		for j in xrange(4):
			if board[i][j] == ".":
				return True
	return False

def result(board):
	if checkWin(board, "XT"):
		return "X won"
	if checkWin(board, "OT"):
		return "O won"
	if checkFree(board):
		return "Game has not completed"
	return "Draw"

for t in xrange(1,T+1):
	board = [f.readline().strip() for i in xrange(4)]
	f.readline()
	print "Case #{0}: {1}".format(t, result(board))
