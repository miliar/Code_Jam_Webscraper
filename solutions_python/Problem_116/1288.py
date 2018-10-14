import sys
import time
import math

with open(sys.argv[1]) as f:
	T  = int(f.readline())
	content = f.readlines()

def vline(board, x):
	return [board[y][x] for y in range(4)]

def hline(board, x):
	return [board[x][y] for y in range(4)]

def dline(board, nope):
	return [board[y][y] for y in range(4)]

def ddline(board, nope):
	return [board[y][3-y] for y in range(4)]


for t in range(T):
	board = [r[0:4] for r in content[t*5:t*5+4]]
	dots = sum([1 if board[x][y] == '.' else 0 for x in range(4) for y in range(4)])
	X = False
	O = False
	def win(func, board, i):
		x = 0
		o = 0
		line = func(board,i)
		for l in line:
			x = x + 1 if l in ['X','T'] else x
			o = o + 1 if l in ['O','T'] else o
		if x == 4 or o == 4:
			return 'X' if x == 4 else 'O'
		return False

	for x in range(4):
		for f in [vline,hline]:
			sign = win(f, board, x) 
			O = O or sign == 'O'
			X = X or sign == 'X'
	sign = win(dline, board, 1) 
	O = O or sign == 'O'
	X = X or sign == 'X'

	sign = win(ddline, board, 1) 
	O = O or sign == 'O'
	X = X or sign == 'X'
	
	if dots > 0:
		status = "Game has not completed"
	if O:
		status = 'O won'
	if X:
		status = 'X won'
	if X and O:
		status = 'Draw'
	if not X and not O and dots == 0:
		status = "Draw"


	print "Case #%d: %s" % (t+1,status)

