#!/usr/bin/python

def readGame(fp):
	game = []

	for i in range(4):
		line = fp.readline()
		game.append(line[:-1]) # remove '\n'

	fp.readline() # dismiss empty line
	return game

def getFirstChar(line):
	if line[0] == 'T':
		return line[1]
	return line[0]

def getChampion(sequence):
	for char in sequence:
		if char != 'T':
			return char

def checkEnding(line):
	sequence = [getFirstChar(line)]
	for char in line[1:]:
		if (char in sequence or char == 'T') and (char != '.'):
			sequence.append(char)
	if len(sequence) == 4:
		#print 'Game finished with sequence', sequence
		return getChampion(sequence)
	return None

def checkHorizontal(game):
	for line in game:
		char = checkEnding(line)
		if char:
			return char
	return None

def checkDiagonal(game):
	line = ''.join(game[i][i] for i in range(4))
	return checkEnding(line)

def checkOppositeDiagonal(game):
	line = ''.join(game[3 - i][i] for i in range(4))
	return checkEnding(line)

def checkFull(game):
	for line in game:
		if '.' in line:
			#print 'Game has not completed'
			return False
	return True

def transpose(game):
	return [''.join([game[j][i] for j in range(4)]) for i in range(4)]

def checkGame(game):
	# check horizontal
	winner = checkHorizontal(game)
	if winner:
		return (winner + ' won')
	# check vertical
	winner = checkHorizontal(transpose(game))
	if winner:
		return (winner + ' won')
	# check diagonal
	winner = checkDiagonal(game)
	if winner:
		return (winner + ' won')
	# check opposite diagonal
	winner = checkOppositeDiagonal(game)
	if winner:
		return (winner + ' won')
	# check game has finished
	if checkFull(game):
		return 'Draw'
	return 'Game has not completed'

# Open file
fp = open('A-large.in')
cases = int(fp.readline())
#print '#Cases:', cases

# Open output file
fpout = open('output.txt', 'w')

#for i in range(1):
for i in range(cases):
	game = readGame(fp)
	output = 'Case #%d: %s' %(i + 1, checkGame(game))
	fpout.write(output + '\n')
	print output
	