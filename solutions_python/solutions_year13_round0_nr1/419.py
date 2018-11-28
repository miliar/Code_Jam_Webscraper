import os
import sys


def recognize_(a,b,c,d):
	xcount=0
	tcount=0
	ocount=0
	if a=='X':
		xcount+=1 
	elif a=='T':
		tcount+=1
	elif a=='O':
		ocount+=1
	if b=='X':         
                xcount+=1
        elif b=='T':
                tcount+=1
        elif b=='O':
                ocount+=1
	if c=='X':         
                xcount+=1
        elif c=='T':
                tcount+=1
        elif c=='O':
                ocount+=1
	if d=='X':         
                xcount+=1
        elif d=='T':
                tcount+=1
        elif d=='O':
                ocount+=1
	if xcount==3 and tcount==1 or xcount==4:
		return 'X'
	if ocount==3 and tcount==1 or ocount==4:
		return 'O'
	return None
def recognize(board):
	#checking rows and columns
	for i in range(4):
		winner=recognize_(board[i][0],board[i][1],board[i][2],board[i][3])
		if winner!=None:
			return winner+' won'
		winner=recognize_(board[0][i],board[1][i],board[2][i],board[3][i])
		if winner!=None:
                        return winner+' won'
	#checking diagonals
	winner=recognize_(board[0][0],board[1][1],board[2][2],board[3][3])
	if winner!=None:
		return winner+' won'
	winner=recognize_(board[3][0],board[2][1],board[1][2],board[0][3])
	if winner!=None:
        	return winner+' won'
	#checking if the board contains .
	for i in board:
		for j in i:
			if j=='.':
				return 'Game has not completed'
	return 'Draw'

lines=sys.stdin.readlines()

board=[]
cnt=0
for line in lines[1:]:
	
	if line!='\n':
		board.append(line)
	else:
		cnt+=1
		print 'Case #'+str(cnt)+': '+recognize(board)
		board=[]
