#!/bin/env python
#-*- coding: utf_8 -*-


#############
# functions #
#############
def wins (board, who, t):
	if len (t) > 0:
		board[t[0]][t[1]] = who
	for row in range (4):
		row_ok = True
		for col in range (4):
			if board[row][col] != who:
				row_ok = False
				break
		if row_ok:
			if len (t) > 0:
				board[t[0]][t[1]] = 'T'
			return True
	for col in range (4):
		col_ok = True
		for row in range (4):
			if board[row][col] != who:
				col_ok = False
				break
		if col_ok:
			if len (t) > 0:
				board[t[0]][t[1]] = 'T'
			return True
	if board[0][0] == who and board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == board[3][3]:
		if len (t) > 0:
			board[t[0]][t[1]] = 'T'
		return True
	if board[3][0] == who and board[3][0] == board[2][1] and board[2][1] == board[1][2] and board[1][2] == board[0][3]:
		if len (t) > 0:
			board[t[0]][t[1]] = 'T'
		return True
	if len (t) > 0:
		board[t[0]][t[1]] = 'T'
	return False


import sys
if len (sys.argv) > 1:
	sys.stdin = open (sys.argv[1], 'r')


for case in range (int (raw_input().strip())):
	case += 1
	board = []
	t = []
	has_empty = False
	for row in range (4):
		line = raw_input().rstrip()
		line_list = map (lambda x: x, line)
		t_col = line.find ('T')
		if t_col >= 0:
			t = [row, t_col]
		has_empty |= (line.find ('.') >= 0)
		board.append (line_list)
	raw_input()
	o_wins = wins (board, 'O', t)
	x_wins = wins (board, 'X', t)
	if o_wins and x_wins:
		print 'Case #%d: Draw' % case
	elif o_wins:
		print 'Case #%d: O won' % case
	elif x_wins:
		print 'Case #%d: X won' % case
	else:
		if has_empty:
			print 'Case #%d: Game has not completed' % case
		else:
			print 'Case #%d: Draw' % case
