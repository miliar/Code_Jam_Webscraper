#!/usr/bin/python

import sys
import math

def read_board(infile):
	board = []
	for i in range(4):
		board.append([x for x in infile.readline().strip()])

	infile.readline()
	return board

def get_lines(board):
	lines = []
	for i in range(4):
		lines.append(board[i])
		lines.append([board[x][i] for x in range(4)])

	lines.append([board[x][x] for x in range(4)])
	lines.append([board[3 - x][x] for x in reversed(range(4))])

	return lines	

def check_winner(lines, board):
	set_O_wins = set(['O', 'T'])
	set_X_wins = set(['X', 'T'])
	for line in lines:
		if set(line + ['T']) == set_O_wins:
			return 'O won'
		elif set(line + ['T']) == set_X_wins:
			return 'X won'

	for i in range(4):
		if '.' in board[i]:
			return 'Game has not completed'

	return 'Draw'

if __name__ == '__main__':
	filename = sys.argv[1]

	try:
		infile = open(filename)
	except:
		print "Couldn't open file: %s" % filename
		sys.exit(1)

	numcases = int(infile.readline())

	for case in range(1, numcases + 1):

		board = read_board(infile)
		lines = get_lines(board)
		outcome = check_winner(lines, board)

		print "Case #%s: %s" % (case, outcome)

