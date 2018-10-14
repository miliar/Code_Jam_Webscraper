import string
import math

def gameNotCompleted(lines):
	for x in range(4):
		for y in range(4):
			if(lines[x][y] == '.'):
				return True
	return False

def win(lines, x):
	win = False
	#Check vertically
	for i in range(4):
		lineGood = True
		for y in range(4):
			if lines[i][y] != x and lines[i][y] != 'T' :
				lineGood = False
				break
		if lineGood :
			return True

	
	#Check horizontally
	for i in range(4):
		lineGood = True
		for y in range(4):
			if lines[y][i] != x and lines[y][i] != 'T' :
				lineGood = False
				break
		if lineGood :
			return True

	#check diagonals
	lineGood = True
	for i in range(4):
		if lines[i][i] != x and lines[i][i] != 'T' :
			lineGood = False
			break
	if lineGood :
		return True	
		
	lineGood = True
	for i in range(4):
		if lines[3-i][i] != x and lines[3-i][i] != 'T' :
			lineGood = False
			break
 
	if lineGood :
		return True

	return False

#Main function
inFile = open('input.txt', 'r')
numCases = int(inFile.readline())
outFile = open('output.txt', 'w')
for i in range(numCases):
	outFile.write("Case #")
	outFile.write(str(i + 1))
	outFile.write(": ")
	lines = [""]*4
	for x in range(4):
		lines[x] = inFile.readline()
	#Now lines has the whole board			
	#Check X for wins
	xWins = win(lines, 'X')
	oWins = win(lines, 'O')	
	if xWins :
		outFile.write("X won")
	#Check O for wins
	elif oWins :
		outFile.write("O won")
	elif gameNotCompleted(lines) :
		outFile.write("Game has not completed")
	else:
		outFile.write("Draw")

	outFile.write("\n")
	inFile.readline()
