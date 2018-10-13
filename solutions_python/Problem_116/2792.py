def checkBoard(board):
	def checkLine(line):
		if line=='XXXT' or line=='TXXX' or line=='XXXX':
			return "X won"
		elif line=='OOOT' or line=='TOOO' or line=='OOOO':
			return "O won"
		else: return "moreCheck"
	for row in board:
		#print "{0}:{1}".format(row,checkLine(row))
		if checkLine(row)!="moreCheck": return checkLine(row)
	board=[list(row) for row in board]
	for i in range(4):
		col= "".join([board[0][i],board[1][i],board[2][i],board[3][i]])
		if checkLine(col)!="moreCheck": return checkLine(col)
	ld="".join(board[j][j] for j in range(4))
	if checkLine(ld)!="moreCheck": return checkLine(ld)
	rd="".join(board[j][3-j] for j in range(4))
	if checkLine(rd)!="moreCheck": return checkLine(rd)
	for k in range(4):
		for l in range(4):
			if board[k][l]==".": return "Game has not completed"
	return "Draw"
T = int(raw_input())
for t in range(T):
	board = [raw_input(), raw_input(), raw_input(), raw_input()]
	ignore = raw_input()
	result = checkBoard(board)
	print 'Case #{0}: {1}'.format(t+1, result)
