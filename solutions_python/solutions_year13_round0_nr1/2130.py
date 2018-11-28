

def loadGames(filename):
	def lineToList(line):
		line = line.replace('\n','')
		return [ ch for ch in line ]

	f = open(filename, 'r')
	targetSize = int(f.readline())
	lines = [ lineToList(l) for l in f.readlines() if not l == '\n' ]
	games = []
	i = 0
	while len(games) < targetSize:
		game = []
		for ii in xrange(4):
			game.append(lines[i*4+ii])
		games.append(game)
		i += 1
	return games

def scoreGame(game):
	def scoreLine(line):
		assert len(line) == 4
		if '.' in line:
			return False
		if 'O' in line and not 'X' in line:
			return 'O won'
		if 'X' in line and not 'O' in line:
			return 'X won'
		return False

	for i in xrange(4):
		if not scoreLine(game[i]) == False:
			return scoreLine(game[i])

		line = []
		for ii in xrange(4):
			line.append(game[ii][i])
		if not scoreLine(line) == False:
			return scoreLine(line)

	line = []
	for i in xrange(4):
		line.append(game[i][i])
	if not scoreLine(line) == False:
		return scoreLine(line)

	line = [game[0][3],game[1][2],game[2][1], game[3][0]]
	if not scoreLine(line) == False:
		return scoreLine(line)

	if filter( lambda x : '.' in x, game) == []:
		return 'Draw'
	else:
		return 'Game has not completed'


def run():
	games = loadGames('A-large.in')
	s = ""
	for i in xrange(len(games)):
		s = s + "Case #" + str(i+1) + ": " + scoreGame(games[i]) + "\n"
	f = open('A-large.out','w')
	f.write(s)
	f.close


run()
