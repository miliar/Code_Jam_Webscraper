#!/usr/bin/python

xwin="X won"
owin="O won"
draw="Draw"
incomplete="Game has not completed"

N=4

def checkRow(board,row,char):
	count=0
	for i in range(0,N):
		if(board[row][i]==char or board[row][i]=='T'):
			count = count+1
	if(count==N):
		return True

def checkCol(board,col,char):
	count=0
	for i in range(0,N):
		if(board[i][col]==char or board[i][col]=='T'):
			count = count+1
	if(count==N):
		return True

def checkPrincipalDiag(board,char):
	count=0
	for i in range(0,N):
		if(board[i][i]==char or board[i][i]=='T'):
			count = count+1
	if(count==N):
		return True

def checkOtherDiag(board,char):
	count=0
	for i in range(0,N):
		if(board[N-i-1][i]==char or board[N-i-1][i]=='T'):
			count = count+1
	if(count==N):
		return True

def checkWin(board,case):
	count=0
	#for Game not completed
	for i in range(0,N):
		for j in range(0,N):
			if(board[i][j]=='X' or board[i][j]=='O' or board[i][j]=='T'):
				count=count+1
	#For X
	for i in range(0,N):
		if(checkRow(board,i,'X') or checkCol(board,i,'X')):
			print "Case #"+str(case)+": "+xwin
			return
	if(checkPrincipalDiag(board,'X') or checkOtherDiag(board,'X')):
		print "Case #"+str(case)+": "+xwin
		return
	#For O
	for i in range(0,N):
		if(checkRow(board,i,'O') or checkCol(board,i,'O')):
			print "Case #"+str(case)+": "+owin
			return
	if(checkPrincipalDiag(board,'O') or checkOtherDiag(board,'O')):
		print "Case #"+str(case)+": "+owin
		return
	if(count<16):
		print "Case #"+str(case)+": "+incomplete
	else:
		print "Case #"+str(case)+": "+draw

T = int(raw_input())
board=[[0]*N]*N

for case in range(1,T+1):
	board[0] = list(raw_input())
	board[1] = list(raw_input())
	board[2] = list(raw_input())
	board[3] = list(raw_input())
	checkWin(board,case)
	# Read blank line
	try:
		raw_input()
	except EOFError:
		0
