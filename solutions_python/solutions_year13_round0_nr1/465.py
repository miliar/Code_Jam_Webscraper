#!/usr/bin/python
import sys

def winner(board_orig, symbol):
	ok = [True] * 10  # 10 combinations
	board = []
	for row in board_orig:
		board.append( row.replace('T', symbol) )
	for i in range(4):
		for j in range(4):
			ok[i] = ok[i] and symbol == board[i][j] == board[i][0]  # row
			ok[4 + i] = ok[4 + i] and symbol == board[j][i] == board[0][i]  # col
		ok[8] = ok[8] and symbol == board[i][i] == board[0][0]  # 1st diagonal
		ok[9] = ok[9] and symbol == board[i][3 - i] == board[3][0]  # 2nd diagonal
	#print 'ok: ', ok
	return True in ok

tcs = int( sys.stdin.readline() )
for tc in range(tcs):
	# read data
	space = False
	board = []
	for row in range(4):
		line = sys.stdin.readline()
		space = space or line.find('.') > -1
		board.append(line)
	sys.stdin.readline()  # empty

	# process
	result = None
	for s in ['X', 'O']:
		if winner(board, s): result = s + ' won'
	if not result:
		result = "Game has not completed" if space else "Draw"

	print "Case #%d: %s" % ((tc + 1), result)

