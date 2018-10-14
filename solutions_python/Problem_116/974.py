import sys
sys.path.append('../..')
from codejam import get, result

def testHV(board,player):
	for t in range(2):
		for x in range(4):
			r=0
			for y in range(4):
				if t==0:
					a,b=x,y
				else:
					a,b=y,x
				if board[a][b]==player or board[a][b]=='T':
					r=r+1
			if r==4: return True
	return False

def testDiag(board,player):
	for t in range(2):
		r=0
		for i in range(4):
			if t==0:
				a,b=i,i
			else:
				a,b=3-i,i
			if board[a][b]==player or board[a][b] == 'T':
				r=r+1
		if r==4: return True
	return False

def testPlayer(board, player):
	#print player
	#print testHV   (board, player)
	#print testDiag (board, player)
	if testHV   (board, player): return True
	if testDiag (board, player): return True
	return False

def full(board):
	for x in range(4):
		for y in range(4):
			if board[x][y] == '.': return False
	return True

cases=get.int()
for iCase in range(cases):
	board=get.strLines(4)
	blank=get.str()
	X=testPlayer(board,'X')
	O=testPlayer(board,'O')
	if X:
		result(iCase, 'X won')
	elif O:
		result(iCase, 'O won')
	elif full(board):
		result(iCase, 'Draw')
	else:
		result(iCase, 'Game has not completed')

