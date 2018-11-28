def isCompleted(board):
	i = 0
	j = 0
	while (i<4):
		while (j<4):
			if(board[i][j] == '.'):
				return False
			j += 1
		i += 1
		j = 0
	return True

def checkHorizontal(board,i):	
	if board[i][0] == 'X' or board[i][0] == 'T':
		if board[i][1] == 'X' or board[i][1] == 'T':
			if board[i][2] == 'X' or board[i][2] == 'T':
				if board[i][3] == 'X' or board[i][3] == 'T':
					return 'X'
				else:
					return False
			else:
				return False
		else:
			return False

	elif board[i][0] == 'O' or board[i][0] == 'T':
		if board[i][1] == 'O' or board[i][1] == 'T':
			if board[i][2] == 'O' or board[i][2] == 'T':
				if board[i][3] == 'O' or board[i][3] == 'T':
					return 'O'
				else:
					return False
			else:
				return False
		else:
			return False


def checkVertical (board,i):
	if board[0][i] == 'X' or board[0][i] == 'T':
		if board[1][i] == 'X' or board[1][i] == 'T':
			if board[2][i] == 'X' or board[2][i] == 'T':
				if board[3][i] == 'X' or board[3][i] == 'T':
					return 'X'
				else:
					return False
			else:
				return False
		else:
			return False

	elif board[0][i] == 'O' or board[0][i] == 'T':
		if board[1][i] == 'O' or board[1][i] == 'T':
			if board[2][i] == 'O' or board[2][i] == 'T':
				if board[3][i] == 'O' or board[3][i] == 'T':
					return 'O'
				else:
					return False
			else:
				return False
		else:
			return False

def checkDiagonal(board):
	if board[0][0] == 'X' or board[0][0] == 'T':
		if board[1][1] == 'X' or board[1][1] == 'T':
			if board[2][2] == 'X' or board[2][2] == 'T':
				if board[3][3] == 'X' or board[3][3] == 'T':
					return 'X'
				else:
					return False
			else:
				return False
		else:
			return False

	elif board[0][0] == 'O' or board[0][0] == 'T':
		if board[1][1] == 'O' or board[1][1] == 'T':
			if board[2][2] == 'O' or board[2][2] == 'T':
				if board[3][3] == 'O' or board[3][3] == 'T':
					return 'O'
				else:
					return False
			else:
				return False
		else:
			return False

def checkInverse(board):
	if board[0][3] == 'X' or board[0][3] == 'T':
		if board[1][2] == 'X' or board[1][2] == 'T':
			if board[2][1] == 'X' or board[2][1] == 'T':
				if board[3][0] == 'X' or board[3][0] == 'T':
					return 'X'
				else:
					return False
			else:
				return False
		else:
			return False

	elif board[0][3] == 'O' or board[0][3] == 'T':
		if board[1][2] == 'O' or board[1][2] == 'T':
			if board[2][1] == 'O' or board[2][1] == 'T':
				if board[3][0] == 'O' or board[3][0] == 'T':
					return 'O'
				else:
					return False
			else:
				return False
		else:
			return False



f = open('A-small-attempt2.in','r')
o = open('output.txt','w')

n = f.readline()
n = int(n)

for case in range(1,n+1):
	board = [[],[],[],[]]
	i = 0
	while (i < 4):
		board[i]=f.readline()
		board[i]=board[i][:4]
		i += 1

	f.readline()

	i = 0
	winner = False

	while (i<4):
		if ( checkHorizontal(board,i) == 'X' ):
			o.write("Case #" + str(case) + ": X won\n")
			winner = True
			break
		elif (checkHorizontal(board,i) == 'O' ):
			o.write("Case #" + str(case) + ": O won\n")
			winner = True
			break
		elif (checkVertical(board,i) == 'X'):
			o.write("Case #" + str(case) + ": X won\n")
			winner = True
			break
		elif (checkVertical(board,i) == 'O'):
			o.write("Case #" + str(case) + ": O won\n")
			winner = True
			break
		elif (checkDiagonal(board) == 'X'):
			o.write("Case #" + str(case) + ": X won\n")
			winner = True
			break
		elif (checkDiagonal(board) == 'O'):
			o.write("Case #" + str(case) + ": O won\n")
			winner = True
			break
		elif (checkInverse(board) == 'X'):
			o.write("Case #" + str(case) + ": X won\n")
			winner = True
			break
		elif (checkInverse(board) == 'O'):
			o.write("Case #" + str(case) + ": O won\n")
			winner = True
			break

		i += 1

	if (winner != True):
		if (isCompleted(board)):
			o.write("Case #" + str(case) + ": Draw\n")
		else:
			o.write("Case #" + str(case) + ": Game has not completed\n")		
		


f.close()
o.close()





