def isWiningRow(game, i, player):
	for j in xrange(4):
		if game[i][j] != player and game[i][j] != 'T':
			return False
	return True

def isWiningColmun(game, j, player):
	for i in xrange(4):
		if game[i][j] != player and game[i][j] != 'T':
			return False
	return True

def isWiningDiagonal1(game, player):
	for i in xrange(4):
		if game[i][i] != player and game[i][i] != 'T':
			return False
	return True

def isWiningDiagonal2(game, player):
	for i in xrange(4):
		if game[i][3-i] != player and game[i][3-i] != 'T':
			print 'False' + game[i][3-i]
			return False
	print 'True'
	return True

def isDraw(game):
	for i in xrange(4):
		for j in xrange(4):
			if game[i][j] == '.':
				return False
	return True

def getGameState(game):
	for i in xrange(4):
		if isWiningRow(game, i, 'X'):
			return 'X'
		if isWiningRow(game, i, 'O'):
			return 'O'
		if isWiningColmun(game, i, 'X'):
			return 'X'
		if isWiningColmun(game, i, 'O'):
			return 'O'
	if isWiningDiagonal1(game, 'X'):
		return 'X'
	if isWiningDiagonal1(game, 'O'):
		return 'O'
	print 'start X'
	if isWiningDiagonal2(game, 'X'):
		return 'X'
	print 'start O'
	if isWiningDiagonal2(game, 'O'):
		return 'O'
	if isDraw(game):
		return 'D'
	return 'G'

fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')
T = int(fin.readline())
for t in xrange(T):
	game = [fin.readline() for x in xrange(4)]
	fin.readline()
	print t
	state = getGameState(game)
	print '#'*10
	fout.write("Case #" + str(t + 1) + ": " + {'X':'X won', 'O':'O won', 'D':'Draw', 'G':'Game has not completed'}[state] + '\n')
fin.close()
fout.close()

