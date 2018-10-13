#!/usr/bin/env python

import sys
import string

fname=sys.argv[1]

i=open(fname,'r')
o=open(fname+'.out','w')

'''readline Split'''
def rls(i):
	out=map(int, string.split(i.readline()))
	return out[0] if len(out)==1 else out

'''Output Case#...'''
def wout(o, i, arg):
	out="Case #"+ str(i)+":"
	out+=" "+str(arg)
	#out+=" "+''.join(arg)
	#for arg in args:
	#    out+=" "+str(arg)
	out+="\n"
	o.write(out)

T=rls(i)

for x in range(T):
	board = [i.readline()[0:4] for j in range(4)]
#	print board
	i.readline()
	#horizontal
	hasdot=False
	for j in range(4):
		O,X=0,0;
		for l in range(4):
			cell=board[j][l]
			if cell == 'O':
				O+=1 
			elif cell == 'X':
				X+=1
			elif cell == 'T':
				O+=1
				X+=1
			elif cell == '.':
				hasdot=True 
				continue
		if O==4 or X==4:
			break;
		O,X=0,0;
		for l in range(4):
			cell=board[l][j]
			if cell == 'O':
				O+=1 
			elif cell == 'X':
				X+=1
			elif cell == 'T':
				O+=1
				X+=1
			elif cell == '.':
				hasdot=True 
				continue
		if O==4 or X==4:
			break;			

	if O!=4 and X!=4:
		# diagonal
		X1,X2,O1,O2=0,0,0,0
		for l in range(4):
			cell1=board[l][l]
			cell2=board[l][3-l]
			if cell1 == 'O':
				O1+=1 
			elif cell1 == 'X':
				X1+=1
			elif cell1 == 'T':
				O1+=1
				X1+=1
			if cell2 == 'O':
				O2+=1 
			elif cell2 == 'X':
				X2+=1
			elif cell2 == 'T':
				O2+=1
				X2+=1
			if cell1 == '.' or cell2 == '.':
				hasdot=True 
			
		if O1==4 or O2==4:
			O=4
		if X1==4 or X2==4:
			X=4
					
	if O==4:
		wout(o, x+1, "O won")
	elif X==4:
		wout(o, x+1, "X won")
	elif hasdot:
		wout(o, x+1, "Game has not completed")
	else:
		wout(o, x+1, "Draw")
