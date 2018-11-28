def check_horizontal(board, line):
	ref = None
	for i in xrange(4):
		if(board[line][i]!='.' and board[line][i]!='T'):
			ref = board[line][i]
	if ref == None: return False
	for i in xrange(4):
		if (board[line][i]!=ref):
			if(board[line][i]!="T"): return False
	return ref
	
def check_vertical(board, line):
	ref = None
	for i in xrange(4):
		if(board[i][line]!='.' and board[i][line]!='T'):
			ref = board[i][line]
	if ref == None: return False
	for i in xrange(4):
		if (board[i][line]!=ref):
			if(board[i][line]!="T"): return False
	return ref

def check_diagonal1(board):
	ref = None
	for i in xrange(4):
		if(board[i][i]!='.' and board[i][i]!='T'):
			ref = board[i][i]
	if ref == None: return False
	
	for i in xrange(4):
		if board[i][i]!=ref:
			if board[i][i]!='T': return False
	return ref
	
def check_diagonal2(board):
	ref = None
	for i in xrange(4):
		if(board[i][3-i]!='.' and board[i][3-i]!='T'):
			ref = board[i][3-i]
	if ref == None: return False
	
	for i in xrange(4):
		if board[i][3-i] != ref:
			if board[i][3-i]!='T': return False
	return ref
	
def wins(board):
	has_empty = False
	for i in xrange(4):
		for j in xrange(4):
			if(board[j][i]!='.'):
				if(j == 0):
					res = check_vertical(board, i)
					if(res):
						return res
				if(i == 0):
					res = check_horizontal(board, j)
					if(res):
						return res
				if(i == 0 and j == 0):
					res = check_diagonal1(board)
					if(res):
						return res
				if(i == 0 and j == 3):
					res = check_diagonal2(board)
					if(res):
						print i, "d2"
						return res
			else:
				has_empty = True
	if has_empty: return "unfinished"
	else: return "draw"
	
k = input()

for i in xrange(k):
	if(i!=0): raw_input()
	board = []
	for j in xrange(4):
		board.append(raw_input())
	
	res = wins(board)
	if(res == 'O' or res == 'X'): print "Case #" + str(i+1) +": " + res+ " won"
	elif(res == "unfinished"): print "Case #" + str(i+1) +": " + "Game has not completed"
	else: print "Case #" + str(i+1) +": " +"Draw"