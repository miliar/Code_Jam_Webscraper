#!/usr/bin/env python


def test(board):
	x=0
	o=0
	for i in board:
		if i.count('X') == 4 or (i.count('X')==3 and i.find('T')!=-1):
			x=x+1
		if i.count('O') == 4 or (i.count('O')==3 and i.find('T')!=-1):
			o=o+1
	a=board[0][0]+board[1][1]+board[2][2]+board[3][3]
	b=board[0][3]+board[1][2]+board[2][1]+board[3][0]

	if a.count('X') == 4 or (a.count('X')==3 and a.find('T')!=-1):
			x=x+1
	if a.count('O') == 4 or (b.count('O')==3 and b.find('T')!=-1):
			o=o+1
	if b.count('X') == 4 or (a.count('X')==3 and a.find('T')!=-1):
			x=x+1
	if b.count('O') == 4 or (b.count('O')==3 and b.find('T')!=-1):
			o=o+1
			
			
	l=[board[0][0]+board[1][0]+board[2][0]+board[3][0],
	   board[0][1]+board[1][1]+board[2][1]+board[3][1],
	   board[0][2]+board[1][2]+board[2][2]+board[3][2],
	   board[0][3]+board[1][3]+board[2][3]+board[3][3]]
	#print l,board
	#print a,b
	for i in l:
		if i.count('X') == 4 or (i.count('X')==3 and i.find('T')!=-1):
			x=x+1
		if i.count('O') == 4 or (i.count('O')==3 and i.find('T')!=-1):
			o=o+1

	if x+o == 0:
		dots=0
		for i in board:
			dots=dots+i.count('.')
	

	if x>o:
		return "X won"
	if x<o:
		return "O won"
	if dots>0:
		return "Game has not completed"
	return "Draw"



if __name__=='__main__':
	fp=open("input.txt","r")
	n=int(fp.readline())
	case=1
	for n in range(0,n):
		l=[]
		for j in range(0,4):
			l.append(fp.readline().strip())
		print "Case #"+str(case)+":",test(l)
		case=case+1
		fp.readline()
	
	
