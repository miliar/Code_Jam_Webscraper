import sys


def mark(casenum, state):
	print "Case #" + str(casenum) + ": " + state


def check_board(board):
	side = len(board)
	#Check rows for wins
	for row in board:
		X=0
		O=0
		for i in range(side):
			if row[i] == 'X':
				X = X+1
			if row[i] == 'O':
				O = O+1
			if row[i] == 'T':
				X = X+1
				O = O+1
		if X == side:
			return 'X won'
		if O == side:
			return 'O won'
	
	#Check columns for wins
	for col in range(side):
		X = 0
		O = 0
		for row in range(side):
			if board[row][col] == 'X':
				X = X+1
			if board[row][col] == 'O':
				O = O+1
			if board[row][col] == 'T':
				X = X+1
				O = O+1
		if X == side:
			return 'X won'
		if O == side:
			return 'O won'
	
	#Check diagonals
	X = 0
	O = 0
	for i in range(side):
		if board[i][i] == 'X':
			X = X+1
		if board[i][i] == 'O':
			O = O+1
		if board[i][i] == 'T':
			X = X+1
			O = O+1
	if X == side:
		return 'X won'
	if O == side:
		return 'O won'

	X = 0
	O = 0
	for i in range(side):
		if board[i][-i-1] == 'X':
			X = X+1
		if board[i][-i-1] == 'O':
			O = O+1
		if board[i][-i-1] == 'T':
			X = X+1
			O = O+1
	
	if X == side:
		return 'X won'
	if O == side:
		return 'O won'
		

	#Check for incomplete
	for row in board:
		for entry in row:
			if entry == '.':
				return 'Game has not completed'
	return 'Draw'

if len(sys.argv) < 2 :
	print "Please enter file name\n"
	exit(0)

fname = sys.argv[1]
stream = open(fname)

input_data = stream.read()

input_data = input_data.split('\n')
	

test_cases = int(input_data[0])

for i in range(test_cases) :
	offset = i*5+1
	board = []
	for j in range(4):
		board.append(input_data[offset+j])
	
	mark(i+1, check_board(board))
