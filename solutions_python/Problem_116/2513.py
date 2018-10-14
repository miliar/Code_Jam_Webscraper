#!/usr/bin/python

from sys import stdin 

def getAnswer(board):
	emptyCell = False
	Xcount = [0, 0]
	Ycount = [0, 0]
	diagCount = [0, 0, 0, 0]  # [xF,yF,xB,yB]
	
	for x in range(4):
		for y in range(4):
			# print x,y
			if(board[x][y] == '.'):
				emptyCell = True
				
			if(board[x][y] == 'X' or board[x][y] == 'T'):
				if(x == y):
					diagCount[0] += 1
				elif(x + y == 3):
					diagCount[2] += 1
				Xcount[0] += 1
			if(board[x][y] == 'O' or board[x][y] == 'T'):
				if(x == y):
					diagCount[1] += 1
				elif(x + y == 3):
					diagCount[3] += 1
				Xcount[1] += 1

			if(board[y][x] == 'X' or board[y][x] == 'T'):
				Ycount[0] += 1
			if(board[y][x] == 'O' or board[y][x] == 'T'):
				Ycount[1] += 1
			if(Xcount[0] == 4 or Ycount[0] == 4):
				return "X won"
			if(Xcount[1] == 4 or Ycount[1] == 4):
				return "O won"
		Xcount = [0, 0]
		Ycount = [0, 0]
		
		if(diagCount[0] == 4 or diagCount[2] == 4):
			return "X won"
		if(diagCount[1] == 4 or diagCount[3] == 4):
			return "O won"
		
	return ["Draw", "Game has not completed"][emptyCell]


num = input()
board = [[], [], [], []]
fhdl = open("Output.out","w")
for x in range(num):
	for y in range(4):
		board[y] = list(stdin.readline().rstrip())
	# print board
	fhdl.write("Case #" + str(x + 1) + ": " + getAnswer(board))
	if(x<(num-1)):
		fhdl.write("\n")
	stdin.readline()
fhdl.close()
