import sys

def parseInput():
	cases = []

	data = [x.strip() for x in sys.stdin.readlines()]

	T = int(data.pop(0))
	for i in xrange(T):
		N, K = tuple([int(x) for x in data.pop(0).split(' ')])

		board = []
		for i in xrange(N):
			vert_line = data.pop(0)
			board.append(vert_line)

		cases.append((K, board))

	return cases

def findSeq(seq, board):
	for line in board:
		if line.find(seq) != -1:
			return True

	return False

def isWinner(K, board):

	N = len(board[0])
	seq = "." * K

	# find vertical lines
	if findSeq(seq, board):
		return True

	# find horizontal lines
	board = [''.join([board[i][j] for i in xrange(N)]) for j in xrange(N)]

	if findSeq(seq, board):
		return True

	# find 45-degree lines
	board45 = []
	for col in xrange(2 * N - 1):
		height = N - abs(col - N)
		board45.append(''.join([board[i][height - i - 1] for i in xrange(height)]))

	if findSeq(seq, board45):
		return True

	board45 = []
	for col in xrange(N):
		height = N - col
		board45.append(''.join([board[i][i + col] for i in xrange(height)]))

	for col in xrange(1, N):
		height = N - col
		board45.append(''.join([board[i + col][i] for i in xrange(height)]))

	if findSeq(seq, board45):
		return True


def solve(K, board):

	N = len(board[0])

	# gravity
	red_board = []
	blue_board = []
	for vert_line in board:
		red_line = ""
		blue_line = ""

		for c in reversed(vert_line):
			if c != '.':
				red_line += ('.' if c == "R" else ' ')
				blue_line += ('.' if c == "B" else ' ')

		red_line += ' ' * (N - len(red_line))
		blue_line += ' ' * (N - len(blue_line))

		red_board.append(red_line)
		blue_board.append(blue_line)

	# find winner
	red_wins = isWinner(K, red_board)
	blue_wins = isWinner(K, blue_board)


	if not red_wins and not blue_wins:
		return "Neither"
	elif red_wins and not blue_wins:
		return "Red"
	elif blue_wins and not red_wins:
		return "Blue"
	else:
		return "Both"

cases = parseInput()
for num, case in enumerate(cases):
	result = solve(*case)
	print "Case #" + str(num + 1) + ": " + result
