x = open("A-large.in","r")

def has(board):
	for e in board:
		for i in e:
			if i == '.':
				return True
	return False
	
def diagRight(board):
	tboard = ""
	for i in range(0,4):
		tboard += board[i][i]
	return rowWon([tboard], 0)
	
def diagLeft(board):
	tboard = ""
	for i in range(0,4):
		tboard += board[i][3-i]
	return rowWon([tboard], 0)
	
def rowWon(b, i):
	tc = b[i][0]
	for x in b[i]:
		if tc == 'T' and x != '.':
			tc = x
		elif x == '.' or (x != tc and x != 'T'):
			return False
	return True

def colWon(b, i):
	tc = b[0][i]
	for j in range(1,4):
		if tc == 'T' and b[j][i] != '.':
			tc = b[j][i]
		if b[j][i] == '.' or (b[j][i] != tc and b[j][i] != 'T'):
			return False
	return True

rotNum = int(x.readline().strip())
for z in range(0, rotNum):
	s = "Case #" + str(z+1) + ": "
	board = []
	for i in range(0, 4):
		board.append(x.readline().strip())
	if z < rotNum - 1:
		next(x)
	
	if diagRight(board):
		if board[0][0] == 'T':
			print(s + board[1][1] + " won")
		else:
			print(s + board[0][0] + " won")
		continue
	elif diagLeft(board):
		if board[0][3] == 'T':
			print(s + board[1][2] + " won")
		else:
			print(s + board[0][3] + " won")
		continue
	else:
		for i in range(0, 4):
			if rowWon(board, i):
				if board[i][0] == 'T':
					print(s + board[i][1] + " won")
				else:
					print(s + board[i][0] + " won")
				break
			elif colWon(board, i):
				if board[0][i] == 'T':
					print(s + board[1][i] + " won")
				else:
					print(s + board[0][i] + " won")
				break
			elif i == 3:
				if has(board):
					print(s + 'Game has not completed')
				else:
					print(s + 'Draw')