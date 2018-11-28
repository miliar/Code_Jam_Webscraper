inputName = "inputa"
outputName = "outputa"
f = open(inputName, "r")
out = open(outputName , "w")

def readBoard():
	board = [0,0,0,0]
	for i in range(0,4):
		board[i] = f.readline().strip()
	#skip new line
	f.readline()
	return board


def calculate(board):
	xrow = [0,0,0,0]
	orow = [0,0,0,0]
	xcol = [0,0,0,0]
	ocol = [0,0,0,0]
	xdiag1 , xdiag2 , odiag1 , odiag2 = 0,0,0,0
	gameCompleted = True
	for i in range(0,4):
		for j in range(0,4):
			if board[i][j] == '.':
				gameCompleted = False
			if board[i][j] == 'X' or board[i][j] == 'T':
				xrow[i] += 1
				xcol[j] += 1
				#check diagonals
				if i == j:
					xdiag1 += 1
				if i+j == 3:
					xdiag2 += 1	
			if board[i][j] == 'O' or board[i][j] == 'T':
				orow[i] += 1
				ocol[j] += 1
				#check diagonals
				if i == j:
					odiag1 += 1
				if i+j == 3:
					odiag2 += 1

	#check winner
	if xdiag1 == 4 or xdiag2 == 4:
		return "X won"
	if odiag1 == 4 or odiag2 == 4:
		return "O won"
	for i in range(0,4):
		if xrow[i] == 4 or xcol[i] == 4:
			return "X won"
		if orow[i] == 4 or ocol[i] == 4:
			return "O won"
	
	#check game complete
	if not gameCompleted:
		return "Game has not completed"

	#draw
	return "Draw" 

def solve():
	t = int(f.readline())
	for i in range(1,t+1):
		print i
		board = readBoard()
		print >> out , "Case #"+str(i)+":",calculate(board)
	f.close()
	out.close()

solve()