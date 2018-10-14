import sys

def isOWinner(board):
	return ((board[0][0] in ["O","T"] and board[0][1] in ["O","T"] and board[0][2] in ["O","T"] and board[0][3] in ["O","T"]) or 
	(board[1][0] in ["O","T"] and board[1][1] in ["O","T"] and board[1][2] in ["O","T"] and board[1][3] in ["O","T"]) or 
	(board[2][0] in ["O","T"] and board[2][1] in ["O","T"] and board[2][2] in ["O","T"] and board[2][3] in ["O","T"]) or
	(board[3][0] in ["O","T"] and board[3][1] in ["O","T"] and board[3][2] in ["O","T"] and board[3][3] in ["O","T"]) or
	(board[0][0] in ["O","T"] and board[1][0] in ["O","T"] and board[2][0] in ["O","T"] and board[3][0] in ["O","T"]) or
	(board[0][1] in ["O","T"] and board[1][1] in ["O","T"] and board[2][1] in ["O","T"] and board[3][1] in ["O","T"]) or
	(board[0][2] in ["O","T"] and board[1][2] in ["O","T"] and board[2][2] in ["O","T"] and board[3][2] in ["O","T"]) or
	(board[0][3] in ["O","T"] and board[1][3] in ["O","T"] and board[2][3] in ["O","T"] and board[3][3] in ["O","T"]) or
	(board[0][0] in ["O","T"] and board[1][1] in ["O","T"] and board[2][2] in ["O","T"] and board[3][3] in ["O","T"]) or
	(board[3][0] in ["O","T"] and board[2][1] in ["O","T"] and board[1][2] in ["O","T"] and board[0][3] in ["O","T"]))


def isXWinner(board):
	return ((board[0][0] in ["X","T"] and board[0][1] in ["X","T"] and board[0][2] in ["X","T"] and board[0][3] in ["X","T"]) or 
	(board[1][0] in ["X","T"] and board[1][1] in ["X","T"] and board[1][2] in ["X","T"] and board[1][3] in ["X","T"]) or 
	(board[2][0] in ["X","T"] and board[2][1] in ["X","T"] and board[2][2] in ["X","T"] and board[2][3] in ["X","T"]) or
	(board[3][0] in ["X","T"] and board[3][1] in ["X","T"] and board[3][2] in ["X","T"] and board[3][3] in ["X","T"]) or
	(board[0][0] in ["X","T"] and board[1][0] in ["X","T"] and board[2][0] in ["X","T"] and board[3][0] in ["X","T"]) or
	(board[0][1] in ["X","T"] and board[1][1] in ["X","T"] and board[2][1] in ["X","T"] and board[3][1] in ["X","T"]) or
	(board[0][2] in ["X","T"] and board[1][2] in ["X","T"] and board[2][2] in ["X","T"] and board[3][2] in ["X","T"]) or
	(board[0][3] in ["X","T"] and board[1][3] in ["X","T"] and board[2][3] in ["X","T"] and board[3][3] in ["X","T"]) or
	(board[0][0] in ["X","T"] and board[1][1] in ["X","T"] and board[2][2] in ["X","T"] and board[3][3] in ["X","T"]) or
	(board[3][0] in ["X","T"] and board[2][1] in ["X","T"] and board[1][2] in ["X","T"] and board[0][3] in ["X","T"]))
	

f = open(sys.argv[1], 'r')

cases = f.readline()

#print "Cases: " , cases



for ro in range(int(cases)):
	matrix = [[0 for x in range(4)] for x in range(4)]
	if(ro > 0): 
		f.readline()
	
	for i in range(4):
		line = f.readline()
		ns = list(line.strip())
		for j in range(4):
			if(len(ns) == 4):
				matrix[i][j] = ns[j]

	if(isXWinner(matrix)):
		print "Case #" + str(ro+1) + ": X won"
	if(isOWinner(matrix)):
		print "Case #"+ str(ro+1) + ": O won"
	if( not isXWinner(matrix) and  not isOWinner(matrix)):
		complete = True
		for row in range(4):
			for col in range(4):
				if(matrix[row][col] == '.'):
					complete = False
		if(not complete):
			print "Case #"+ str(ro+1) + ": Game has not completed" 
		else:
			print "Case #" + str(ro+1) + ": Draw"
