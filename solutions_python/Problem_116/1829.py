#! /usr/bin/python
'''
Name: Sravan Bhamidipati
Date: 12th April, 2013
Purpose: 
'''

import sys

array = xrange(0, 4)

def status(board):
	for i in array:
		board.append((board[0][i], board[1][i], board[2][i], board[3][i]))

	board.append((board[0][0], board[1][1], board[2][2], board[3][3]))
	board.append((board[3][0], board[2][1], board[1][2], board[0][3]))

	dots = 0
	for t in board:
		x_s = t.count("X")
		o_s = t.count("O")
		t_s = t.count("T")

		if x_s == 4 or (t_s == 1 and x_s == 3):
			return ": X won"
		elif o_s == 4 or (t_s == 1 and o_s == 3):
			return ": O won"

		dots += t.count(".")

	if dots > 0:
		return ": Game has not completed"
	else:
		return ": Draw"


fd = open(sys.argv[1], "r")

lineNum = 1
case = 1
board = []

for line in fd.readlines():
	if lineNum == 1:
		lineNum += 1
	else:
		if line == "\n":
			output = "Case #" + str(case) + status(board)
			print output
			case += 1
			board = []
		else:
			board.append(tuple(line.strip()))

fd.close()
