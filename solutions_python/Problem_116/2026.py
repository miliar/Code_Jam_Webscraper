#Tic-Tac-Toe-Tomek

import sys, fileinput, math

# Winning bitstrings
winning = {0b1111000000000000,
0b0000111100000000, 
0b0000000011110000,
0b0000000000001111,
0b1000100010001000,
0b0100010001000100,
0b0010001000100010,
0b0001000100010001,
0b1000010000100001, #diags
0b0001001001001000}


def buildBitString(s):
	numOfBlanks = 0
	X = 0b0
	Y = 0b0
	for c in s:
		X = X << 1
		Y = Y << 1
		if (c=='X' or c=='T'):
			X |= 0b1
		if (c=='O' or c=='T'):
			Y |= 0b1
		if (c =='.'):
			numOfBlanks += 1
	return X,Y,numOfBlanks

def getGameEnding(X,Y,numOfBlanks):
	for w in winning:
		if ((X & w) in winning):
			return 'X won'
		if ((Y & w) in winning):
			return 'O won'
	if numOfBlanks > 0:
		return 'Game has not completed'
	else:
		return 'Draw'

def solve():
	#output file
	out = open('output','w') 

	#input file
	filein = fileinput.input()
	#set up test cases
	caseInt = 1
	totalTests = 0
	
	#process
	for line in filein:
		if filein.isfirstline():
			totalTests = int(line)
		else:
			print caseInt
			#read next 4 lines
			X,Y,blanks = buildBitString(line.strip()+filein.readline().strip()+filein.readline().strip()+filein.readline().strip())
			filein.readline()
			outValue = getGameEnding(X,Y,blanks)
			#write out
			out.write('Case #' + str(caseInt) + ': ' + outValue + '\n')
			print 'Case #' + str(caseInt) + ': ' + outValue + '\n'
			caseInt += 1
			if caseInt > totalTests:
				break;
	out.close


solve()
