#!/usr/bin/env python
# Tic-Tac-Toe-Tomek checker

def get_lines(board):
	# Horizontal lines
	lines = board

	# Vertical lines
	for i in range(0, 4):
		lines.append("%s%s%s%s" % (board[0][i], board[1][i], board[2][i], board[3][i]))

	# Diagonals
	lines.append("%s%s%s%s" % (board[0][0], board[1][1], board[2][2], board[3][3]))
	lines.append("%s%s%s%s" % (board[0][3], board[1][2], board[2][1], board[3][0]))
	return lines

def check_board(board):
	lines = get_lines(board)
	incomplete = False

	for line in lines:
		for letter in ("X", "O"):
			count = line.count(letter)
			if count == 4 or (count == 3 and "T" in line):
				return "%s won" % letter
		if "." in line:
			incomplete = True

	if incomplete:
		return "Game has not completed"
	else:
		return "Draw"

def read_board():
	board = []
	for i in range(0, 4):
		board.append(raw_input().strip())
	return board		


# Get cases quantity
cases = int(raw_input())

for i in range(1, cases+1):
	board = read_board()

	print "Case #%d: %s" % (i, check_board(board))

	# eat the empty line
	try:
		raw_input()
	except EOFError:
		pass
