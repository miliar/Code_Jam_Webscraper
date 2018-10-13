import sys
import os


def checkBoard(board):
	res="Draw"
	
	#row:
	for i in range(4):
		xcount = 0
		ocount = 0
		for j in range(4):
			if board[i*4+j]	== 'X':
				xcount += 1
			elif board[i*4+j] == 'O':
				ocount += 1
			elif board[i*4+j] == 'T':
				xcount += 1
				ocount += 1
		
		if xcount == 4:
			res = "X won"
			return res
		elif ocount == 4:
			res = "O won"
			return res

	#col:
	for i in range(4):
		xcount = 0
		ocount = 0
		for j in range(4):
			if board[i+4*j]	== 'X':
				xcount += 1
			elif board[i+4*j] == 'O':
				ocount += 1
			elif board[i+4*j] == 'T':
				xcount += 1
				ocount += 1
		
		if xcount == 4:
			res = "X won"
			return res
		elif ocount == 4:
			res = "O won"
			return res

	#diag
	if (board[0] == 'X' or board[0] == 'T') and (board[5] == 'X' or board[5] == 'T') and (board[10] == 'X' or board[10] == 'T') and (board[15] == 'X' or board[15] == 'T') or (board[3] == 'X' or board[3] == 'T') and (board[6] == 'X' or board[6] == 'T') and (board[9] == 'X' or board[9] == 'T') and (board[12] == 'X' or board[12] == 'T'):
			res = "X won"
			return res
	elif (board[0] == 'O' or board[0] == 'T') and (board[5] == 'O' or board[5] == 'T') and (board[10] == 'O' or board[10] == 'T') and (board[15] == 'O' or board[15] == 'T') or (board[3] == 'O' or board[3] == 'T') and (board[6] == 'O' or board[6] == 'T') and (board[9] == 'O' or board[9] == 'T') and (board[12] == 'O' or board[12] == 'T'):
			res = "O won"
			return res
	
	
	if board.find(".") >= 0:
		res = "Game has not completed"
	
	return res



"""
"X won" (the game is over, and X won)
"O won" (the game is over, and O won)
"Draw" (the game is over, and it ended in a draw)
"Game has not completed" (the game is not over yet)
"""

inp = ""


with open('a.out', 'w') as fo:

	with open(sys.argv[1], 'r') as fi:
		caseno = int(fi.readline())

		for i in range(caseno):
			brd = ""
			if i>0:
				line = fi.readline()
				
			for j in range(4):
				brd += fi.readline().strip()

			fo.write("Case #"+str(i+1)+": "+checkBoard(brd)+"\n")
			
		fi.closed

	fo.closed






