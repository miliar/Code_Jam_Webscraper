import sys

def checkPos(pos,player):
	if pos == player or pos == "T":
		return True
	return False

def checkDraw(board):
	draw = False
	for i in range(4):
		for j in range(4):
			if board[i][j] == ".":
				draw = True
	return draw
	
def check(board,player):
	won = False
	leftdiagwon = True
	rightdiagwon = True
	for i in range(4):
		vertwon = True
		horwon = True
		for j in range(4):
			if not checkPos(board[i][j],player):
				horwon = False
			if not checkPos(board[j][i],player):
				vertwon = False
		if vertwon or horwon:
			won = True
		if not checkPos(board[i][i],player):
			leftdiagwon = False
		if not checkPos(board[i][3-i],player):
			rightdiagwon = False
	if leftdiagwon or rightdiagwon:
		won = True
	return won

f = open(sys.argv[1], "r")
n = int(f.readline().strip())
for i in range(1, n+1):
	sys.stdout.write("Case #" + repr(i) + ": ")
	board = []
	for j in range(4):
		board.append(list(f.readline().strip()))
	f.readline()
	if check(board,"X"):
		sys.stdout.write("X won\n")
		continue
	if check(board,"O"):
		sys.stdout.write("O won\n")
		continue
	if not checkDraw(board):
		sys.stdout.write("Draw\n")
		continue
	sys.stdout.write("Game has not completed\n")