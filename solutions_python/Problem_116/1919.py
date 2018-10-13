def get_winner(line):
	s = set(line)
	if '.' in s:
		return None
	elif s <= set(['X', 'T']):
		return 'X'
	elif s <= set(['O', 'T']):
		return 'O'
	else:
		return None

def game_state(board):
	# Get rows.
	rows = board

	# Get columns.
	transpose = lambda l: map(list, zip(*l))
	cols = transpose(board)

	# Get diagonals.
	diagonal1 = [board[x][x] for x in xrange(4)]
	diagonal2 = [board[x][3 - x] for x in xrange(4)]
	diagonals = [diagonal1, diagonal2]

	# Check for a winner.
	for line in rows + cols + diagonals:
		winner = get_winner(line)
		if winner is not None:
			return '%s won' % winner

	# Check if the game is over.
	for row in board:
		for case in row:
			if case == '.':
				return 'Game has not completed'

	# There is a draw.
	return 'Draw'

T = int(raw_input())
for x in xrange(1, T + 1):
	board = []
	for _ in xrange(4):
		board.append(list(raw_input()))
		assert len(board[-1]) == 4
	assert len(board) == 4
	raw_input()

	y = game_state(board)
	print('Case #%d: %s' % (x, y))
