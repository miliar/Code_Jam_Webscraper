from sys import stdin
from functools import partial
from itertools import chain

def is_winning_line(tokens, line):
	return all(map(lambda t: t in tokens, line))

def is_winning_board(board, tokens):
	rows = board
	columns = zip(*board)
	diagonals = [[board[x][x] for x in range(4)], [board[3-x][x] for x in range(4)]]
	lines = rows + columns + diagonals
	return any(map(partial(is_winning_line, tokens), lines))

n = int(stdin.readline())
for i in range(1, n + 1):
	board = []
	for j in range(4):
		board.append(stdin.readline().rstrip('\n'))
	stdin.readline()
	message = 'Draw'
	if is_winning_board(board, 'XT'):
		message = 'X won'
	elif is_winning_board(board, 'OT'):
		message = 'O won'
	elif any(map(lambda t: t == '.', chain(*board))):
		message = 'Game has not completed'
	print 'Case #%d: %s' % (i, message)
