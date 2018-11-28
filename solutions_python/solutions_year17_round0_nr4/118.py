#usr/bin/python
from __future__ import division
import sys

fin = open(sys.argv[1], "r")
fout = open("D.out", "w")

def score(board):
	score = 0
	if board == []:
		return 0
	for i in range(len(board)):
		if board[i][0] == 'o':
			score += 2
		else:
			score += 1
	return score

def count_plus(board):
	count = 0
	for i in range(len(board)):
		if board[i][0] == '+':
			count += 1
	return count

def count_cross(board):
	count = 0
	for i in range(len(board)):
		if board[i][0] == 'x':
			count += 1
	return count

def not_taken_put_circle(board, r, c):
	if board == []:
		return True
	for i in range(len(board)):
		if board[i][1] == r and board[i][2] == c:
			return False
		if board[i][1] + board[i][2] == r + c and (board[i][0] != 'x'):
			return False
		if board[i][1] - board[i][2] == r - c and (board[i][0] != 'x'):
			return False
		if board[i][1] == r and (board[i][0] != '+'):
			return False
		if board[i][2] == c and (board[i][0] != '+'):
			return False		
	return True	

def not_taken_put_plus(board, r, c):
	if board == []:
		return True
	for i in range(len(board)):
		if board[i][1] == r and board[i][2] == c:
			return False
		if board[i][1] + board[i][2] == r + c and (board[i][0] != 'x'):
			return False
		if board[i][1] - board[i][2] == r - c and (board[i][0] != 'x'):
			return False	
	return True

def not_taken_put_cross(board, r, c):
	for i in range(len(board)):
		if board[i][1] == r and board[i][2] == c:
			return False
		if board[i][1] == r and (board[i][0] != '+'):
			return False
		if board[i][2] == c and (board[i][0] != '+'):
			return False	
	return True	

def taken_put_circle(board, r, c):
	for i in range(len(board)):
		if (board[i][1] == r) and (board[i][0] != '+') and (board[i][2] != c):
			return False
		if (board[i][2] == c) and (board[i][0] != '+') and (board[i][1] != r):
			return False
		if ((board[i][1] - board[i][2])  == (r - c)) and (board[i][0] != 'x') and (board[i][1] != r):
			return False
		if ((board[i][1] + board[i][2])  == (r + c))  and (board[i][0] != 'x') and (board[i][1] != r):
			return False
	return True		

T = int(fin.readline())
for ii in xrange(T):
	n, m = map(int,fin.readline().split(' '))
	board_s = []
	for mm in range(m):
		s, r, c =  fin.readline().split(' ')
		r, c = map (int, (r, c))
		board_s.append([s,r,c])
	
	sol_board_true = []
	board_true = []
	
	board = board_s[:]
	sol_board = []
	


	for r in range(1,n+1):
		for c in range(1,n+1):
			if not_taken_put_cross(board, r, c):
				board.append(['x', r, c])
				sol_board.append(['x', r, c])

		

	for i in range( (n+1)//2):			
		for r in range(1,n+1):
			c = 1 + i
			if not_taken_put_plus(board, r, c):
				board.append(['+', r, c])
				sol_board.append(['+', r, c])
			c = n - i
			if not_taken_put_plus(board, r, c):
				board.append(['+', r, c])
				sol_board.append(['+', r, c])

		for c in range(1,n+1):
			r = 1 + i
			if not_taken_put_plus(board, r, c):
				board.append(['+', r, c])
				sol_board.append(['+', r, c])
			r = n - i
			if not_taken_put_plus(board, r, c):
				board.append(['+', r, c])
				sol_board.append(['+', r, c])						

								
	for i in range(len(board)):
		if board[i][0] != 'o' and taken_put_circle(board, board[i][1], board[i][2]):
			board[i][0] = 'o'
			sol_board.append(['o', board[i][1], board[i][2]])
			if ['+', board[i][1], board[i][2]] in sol_board:
				sol_board.remove(['+', board[i][1], board[i][2]])
			if ['x', board[i][1], board[i][2]] in sol_board:	
				sol_board.remove(['x', board[i][1], board[i][2]])

	if score(board_true) < score(board):
		sol_board_true = sol_board[:]
		board_true = board[:]

					

	if score(board_true) > 2*n:
		print str(ii + 1), score(board_true), n				
	fout.write("Case #" + str(ii+1) + ": " + str(score(board_true)) + ' ' + str(len(sol_board_true)) + "\n")
	for i in range(len(sol_board_true)):
		fout.write(' '.join(map(str,sol_board_true[i])) + "\n")			
	