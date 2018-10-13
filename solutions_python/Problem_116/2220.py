#! /usr/bin/python -tt

import sys

def find_winner(board):
	
	for player in ('X', 'O'):
		
		win = 4 * player
		
		columns = ["".join([row[i] for row in board]) for i in range(0, 4)]
		diag1 = "".join([board[i][i] for i in range(0, 4)])
		diag2 = "".join([board[i][3-i] for i in range(0, 4)])
		
		lines = board + columns + [diag1, diag2]
		
		for r in lines:
			if r.replace("T", player) == win:
				return "%s won" % player
	
	whole_board = "".join(board)
	return "Game has not completed" if "." in whole_board else "Draw"

with sys.stdin as f:
	T = int(f.readline())
	for t in range(1, T+1):
		board = [f.readline().rstrip() for i in range(0, 4)]
		f.readline()

		result = find_winner(board)
		print "Case #%d: %s" % (t, result)
