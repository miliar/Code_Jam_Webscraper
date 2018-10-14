fil = open("alrgin.txt", "r")
T = int(fil.readline())

#def build_board(file1):
#	board = []
#	board.append(file1.readline().split())
#	file1.readline()
#	return board

def winner(board):
	winner = 'Draw'
	for line in board:
		if "." not in line:
			if set(['X','T']).issuperset( line ) and 'O' not in line:
				return 'X won'
			if set(['O','T']).issuperset(line) and 'X' not in line:
				return 'O won'
	dot = 0
	for line in board:
		if '.' in line:
			dot = 1
	if dot is 0:
		return 'Draw'
	else:
		return 'Game has not completed'

def find_winner(board):
	board1 = zip(*board)
	diag1 = [board[0][0], board[1][1], board[2][2], board[3][3]]
	diag2 = [board[0][3], board[1][2], board[2][1], board[3][0]]
	game = [board, board1, [diag1], [diag2]]
	win = []
	for board in game:
		win.append(winner(board))
	#print win
	if 'X won' in win:
		return 'X won'
	elif 'O won' in win:
		return 'O won'
	elif 'Game has not completed' in win:
		return 'Game has not completed'
	else:
		return 'Draw'
		

for k in range(T):
	board = []
	for q in range(4):
		x = list(fil.readline())
		board.append(x[:4])
	fil.readline()
	#print board
	print "Case #%d: %s" % (k+1, find_winner(board))

