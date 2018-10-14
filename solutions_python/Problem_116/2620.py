#!/usr/bin/env python

import sys

def analyse_board(board):
	completed = True
	for row in board:
		if '.' in row:
			completed = False
		if not row.strip('XT'):
			return 'X won'
		if not row.strip('OT'):
			return 'O won'
	for column in zip(*board):
		if '.' in row:
			completed = False
		if not ''.join(column).strip('XT'):
			return 'X won'
		if not ''.join(column).strip('OT'):
			return 'O won'
	diagonal = ''.join([board[0][0], board[1][1], board[2][2], board[3][3]])
	if not diagonal.strip('XT'):
		return 'X won'
	if not diagonal.strip('OT'):
		return 'O won'
	diagonal = ''.join([board[0][3], board[1][2], board[2][1], board[3][0]])
	if not diagonal.strip('XT'):
		return 'X won'
	if not diagonal.strip('OT'):
		return 'O won'
	if completed:
		return 'Draw'
	return 'Game has not completed'
	

with open(sys.argv[1]) as input:
	input.next()
	case = 1
	board = []
	for index, line in enumerate(input):
		if line.strip():
			board += [line.strip()]
		if index % 5 == 3:
			print 'Case #%s: %s' % (case, analyse_board(board))
			board = []
			case += 1

