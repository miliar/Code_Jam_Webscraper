import sys

"""For Small Input File
inFile = open("A-small-attempt0.in", "r")
outFile = open("A-small-attempt0.out", "w")"""

"""For Large Input File"""
inFile = open("A-large.in", "r")
outFile = open("A-large.out", "w")

def verticalCheck(r):
	x = 0
	o = 0
	result = ''
	for i in r:
		x = 0
		o = 0
		for j in i:
			if j == 'X':
				x += 1
			elif j == 'O':
				o += 1
			elif j == 'T':
				x += 1
				o += 1
		if x == 4:
			result = 'X'
			break
		elif o == 4:
			result = 'O'
			break
	return result
				
def horizontalCheck(r):
	x = 0
	o = 0
	result = ''
	for i in range(4):
		x = 0
		o = 0
		for j in range(4):
			if r[j][i] == 'X':
				x += 1
			elif r[j][i] == 'O':
				o += 1
			elif r[j][i] == 'T':
				x += 1
				o += 1
		if x == 4:
			result = 'X'
			break
		elif o == 4:
			result = 'O'
			break
	return result

def diagonalCheck(r):
	x = 0
	o = 0
	result = ''
	for i in range(4):
		if r[i][i] == 'X':
			x += 1
		elif r[i][i] == 'O':
			o += 1
		elif r[i][i] == 'T':
			x += 1
			o += 1
	if x == 4:
		result = 'X'
	elif o == 4:
		result = 'O'
	else:
		x = 0
		o = 0
		result = ''
		j = 3
		for i in range(4):
			if r[i][j] == 'X':
				x += 1
			elif r[i][j] == 'O':
				o += 1
			elif r[i][j] == 'T':
				x += 1
				o += 1
			j -= 1
		if x == 4:
			result = 'X'
		elif o == 4:
			result = 'O'
	
	return result

def emptyCheck(r):
	result = ''
	for i in range(4):
		for j in range(4):
			if r[i][j] == '.':
				result = 'NC'
				break
	return result
	
def outputWrite(case, result):
	if result == 'X':
		outResult = 'X won'
	elif result == 'O':
		outResult = 'O won'
	elif result == 'D':
		outResult = 'Draw'
	else:
		outResult = 'Game has not completed'
	outFile.write("Case #%d: %s" % (case + 1, outResult) + "\n")
	
T = int(inFile.readline())
r = [0]*4
for T in range(T):
	for i in range(4):
		r[i] = inFile.readline().replace('\n', '')
	inFile.readline()
	win = verticalCheck(r);
	if win == 'X':
		outputWrite(T, win)
	elif win == 'O':
		outputWrite(T, win)
	else:
		win = horizontalCheck(r)
		if win == 'X':
			outputWrite(T, win)
		elif win == 'O':
			outputWrite(T, win)
		else:
			win = diagonalCheck(r)
			if win == 'X':
				outputWrite(T, win)
			elif win == 'O':
				outputWrite(T, win)
			else:
				win = emptyCheck(r)
				if win == 'NC':
					outputWrite(T, win)
				else:
					win = 'D'
					outputWrite(T, win)

inFile.close()
outFile.close()