import sys

def solve(board):
	XH = [0,0,0,0]
	XV = [0,0,0,0]
	XD = [0,0]
	OH = [0,0,0,0]
	OV = [0,0,0,0]
	OD = [0,0]
	
	freecell = False
	for i in range(4):
		for j in range(4):
			c = board[i][j]
			if c == ".":
				freecell = True
			if (c == "X" or c == "T"):
				XV[i] += 1
				XH[j] += 1
				if (i == j):
					XD[0] += 1
				if (i+j == 3):
					XD[1] += 1
			if (c == "O" or c == "T"):
				OV[i] += 1
				OH[j] += 1
				if (i == j):
					OD[0] += 1
				if (i+j == 3):
					OD[1] += 1
	xwon = False
	owon = False
	for i in range(4):
		if (XV[i] == 4 or XH[i] == 4 or XD[i%2] == 4):
			xwon = True
		if (OV[i] == 4 or OH[i] == 4 or OD[i%2] == 4):
			owon = True
	
	if xwon:
		if owon:
			return "BOTH"
		else:
			return "X won"
	elif  owon:
		return "O won"
	elif freecell:
		return "Game has not completed"
	else:
		return "Draw"
		
			
			
infile = open(sys.argv[1],'r')
n = int(infile.readline().strip())
for i in range(n):
	board = []
	for j in range(4):
		args = infile.readline().strip()
		row = []
		for k in range(4):
			row.append(args[k])
		board.append(row)
	infile.readline()
	print("Case #" + str(i+1) + ": " + str(solve(board)))
