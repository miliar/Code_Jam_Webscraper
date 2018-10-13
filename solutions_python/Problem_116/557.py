import sys

DEBUG = False;
FILENAME = 'tictac';

def check_for_win(player_letter, board):
	if board[0][0] == board[1][1] == board[2][2] == board[3][3] == player_letter:
		return True
	elif board[3][0] == board[2][1] == board[1][2] == board[0][3] == player_letter:
		return True

	for line in board:
		if line == list(player_letter * 4):
			return True

	for col in range(4):
		if board[0][col] == board[1][col] == board[2][col] == board[3][col] == player_letter:
			return True

	return False

if DEBUG:
	in_file = open(FILENAME + '_example.in')
else:
	in_file = open(FILENAME + '.in')
	sys.stdout = open(FILENAME + '.out', 'w')

num_test_cases = int(in_file.readline().strip())
for case_num in range(num_test_cases):
	#y, x / row, col
	board = []
	for _ in range(4):
		line = list(in_file.readline().strip())
		board.append(line)
	
	output = 'Draw'
	t_row = None
	t_col = None

	for row_num, line in enumerate(board):
		if '.' in line:
			output = 'Game has not completed'
		if 'T' in line:
			t_row = row_num
			t_col = line.index('T')

	if t_row is not None:
		board[t_row][t_col] = 'X'
	x_won = check_for_win('X', board)

	if t_row is not None:
		board[t_row][t_col] = 'O'
	o_won = check_for_win('O', board)

	if x_won:
		output = 'X won'
	elif o_won:
		output = 'O won'

	in_file.readline() # Skip empty line

	print 'Case #' + str(case_num + 1) + ': ' + output
