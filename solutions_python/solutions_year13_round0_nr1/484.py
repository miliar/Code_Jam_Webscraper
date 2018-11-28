def check(board,start,delta,player):
	four = True
	for i in range(4):
		if not board[start[0]+delta[0]*i][start[1]+delta[1]*i] in [player, "T"]:four = False
	return four

for T in xrange(int(raw_input())):
	board = []
	#read input
	for i in range(4):
		board.append(raw_input())
	raw_input()
	winner = ""
	#check for 4 in row, col or diag
	for player in ["X","O"]:
		for i in range(4):
			if check(board,[i,0],[0,1],player): winner = player
			if check(board,[0,i],[1,0],player): winner = player
		if check(board,[0,0],[1,1],player):winner = player
		if check(board,[3,0],[-1,1],player):winner = player
	#create result
	result = ""
	if winner!="":
		if winner == "X":
			result = "X won"
		else:
			result = "O won"
	else:
		# check for filled board
		filled = True
		for i in xrange(4):
			for j in xrange(4):
				if board[i][j]==".": filled = False
		if filled:
			result = "Draw"
		else:
			result = "Game has not completed"
	print "Case #"+str(T+1)+": "+result




