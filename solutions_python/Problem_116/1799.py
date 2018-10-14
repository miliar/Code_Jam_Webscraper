import fileinput
import sys


def contains(board,value):
	for x in range(0,4):
		for y in range(0,4):
			if board[x][y] is value:
				return True
	return False

def findWinner(board):
	for x in range(0,4):
		checking = 'I'
		for y in range(0,4):
			if checking is '.':
				break
			if checking is 'I' or checking is 'T':
   				checking = board[x][y]
			if board[x][y] is checking or board[x][y] is 'T':
   				#print("Board:"+str(board[x][y])+" checking:"+str(checking))
   				if y == 3:
   					#print("X:"+str(x)+" Y:"+str(y))
   					return checking
			else:
   				break
	for y in range(0,4):
		checking = 'I'
		for x in range(0,4):
			if checking is '.':
				break
			if checking is 'I' or checking is 'T':
   				checking = board[x][y]
			if board[x][y] is checking or board[x][y] is 'T':
   				#print("Board:"+str(board[x][y])+" checking:"+str(checking))
   				if x == 3:
   					#print("X:"+str(x)+" Y:"+str(y))
   					return checking
			else:
   				break
	checking = 'I'
	for x in range(0,4):
		if checking is '.':
			break
		if checking is 'I' or checking is 'T':
			checking = board[x][x]
		if board[x][x] is checking or board[x][x] is 'T':
			#print("Board:"+str(board[x][y])+" checking:"+str(checking))
			if x == 3:
				#print("X:"+str(x)+" Y:"+str(y))
				return checking
		else:
			break

	checking = 'I'
	for x in range(0,4):
		if checking is '.':
			break		
		if checking is 'I' or checking is 'T':
			checking = board[x][3-x]
		if board[x][3-x] is checking or board[x][3-x] is 'T':
			#print("Board:"+str(board[x][y])+" checking:"+str(checking))
			if x == 3:
				#print("X:"+str(x)+" Y:"+str(y))
				return checking
		else:
			break

infile=fileinput.input()
numCases=int(infile.readline())

for case in range(1,numCases+1):
	sys.stdout.write("Case #"+str(case)+": ")
	board = [[0 for x in range(4)] for x in range(4)] 
	for x in range(0,4):
		line = infile.readline().strip()
		y=0
		for c in line:
			board[x][y] = c
			y+=1
	infile.readline()
	

	winner = findWinner(board)
	if winner:
		print(winner + " won")
	else:
		if contains(board,'.'):
			print("Game has not completed")
		else:
			print("Draw")
	

