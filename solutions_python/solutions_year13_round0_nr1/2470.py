# tic tac toe tomek

# 4x4 board, initially empty except for a T
# win if: 4 in a row, or 3 with the T
# if all filled, a draw

DEBUG = False

X_WON_STRING = 'X won'
O_WON_STRING = 'O won'
DRAW_STRING = 'Draw'
INCOMPLETE_STRING = 'Game has not completed'

import sys
import os
import time
import copy

DEBUG = True

def readDataFile(fname_in, fname_out):
	fi = open(fname_in, 'rb')
	lines = fi.readlines()
	fi.close()

	# parse the input from lines

	param_T = int( lines[0] )
	n = 1 # the current line number
	
	solutions = []
	for t in range(param_T):
		board = []
		for i in range(4):
			row = []
			for j in range(4):
				row.append(lines[n][j])
				
			board.append( row )
			n += 1
		n += 1 # skip the empty line
		
		if DEBUG:
			print t
			print board
			print
		
		xWins = False
		oWins = False
		draw = True
		
		boardX = copy.deepcopy(board)
		boardO = copy.deepcopy(board)
	
		# check each line for a winner
		for i in range(4):
			for j in range(4):
				if board[i][j] == 'T':
					boardX[i][j] = 'X'
					boardO[i][j] = 'O'
					
			if 'X' == boardX[i][0] == boardX[i][1] == boardX[i][2] == boardX[i][3]:
				xWins = True
			if 'O' == boardO[i][0] == boardO[i][1] == boardO[i][2] == boardO[i][3]:
				oWins = True
			if '.' in board[i]:
				draw = False # game not finished, so can't be a draw yet
		
		# check each col for a winner
		for j in range(4):
			if 'X' == boardX[0][j] == boardX[1][j] == boardX[2][j] == boardX[3][j]:
				xWins = True
			if 'O' == boardO[0][j] == boardO[1][j] == boardO[2][j] == boardO[3][j]:
				oWins = True
				
		# check both diags for winner
		if 'X' == boardX[0][0] == boardX[1][1] == boardX[2][2] == boardX[3][3]:
			xWins = True
		if 'O' == boardO[0][0] == boardO[1][1] == boardO[2][2] == boardO[3][3]:
			oWins = True
			
		if 'X' == boardX[0][3] == boardX[1][2] == boardX[2][1] == boardX[3][0]:
			xWins = True
		if 'O' == boardO[0][3] == boardO[1][2] == boardO[2][1] == boardO[3][0]:
			oWins = True


		# determine winner
		if xWins:
			s = 'X won'
		elif oWins:
			s = 'O won'
		elif not draw:
			s = 'Game has not completed'
		else:
			s = 'Draw'
			
		if DEBUG:
			print 'Case #%d: %s' % (t+1, s)
			print
			
		solutions.append( s )
			
	print
	print 'Results'
	# write out the solutions	
	fo = open(fname_out, 'wb')
	
	for i in range(len(solutions)):	
		s = 'Case #%d: %s' % (i+1, solutions[i])
		fo.write(s + '\n')
		print s
	fo.close()
	
	
def main(argv):
	fname_in = argv[0]
	print 'Processing: ', fname_in
	
	root, _ = os.path.splitext(fname_in)
	fname_out = root + '.out'
	print 'Writing output to: ', fname_out
	
	t0 = time.time()

	readDataFile(fname_in, fname_out)
	print
	print 'Summary:'
	t1 = time.time()
	total = t1 - t0
	print 'Total computation time: %.3f s' % total
	
	print 'Output written to: %s' % fname_out
	
if __name__ == '__main__':
	main(sys.argv[1:])

