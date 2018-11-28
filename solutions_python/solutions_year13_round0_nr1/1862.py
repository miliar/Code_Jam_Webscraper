f = open('A-small-attempt0.bin', 'r')
x = int(f.readline())

def won(game):

	def verify(line):
		if line.count('X') == 4 or (line.count('X') == 3 and 'T' in line):
			return 'X'

		elif line.count('O') == 4 or (line.count('O') == 3 and 'T' in line):
			return 'O'

		else:
			return 'Y'

	for line in game:
		ans = verify(line)
		if ans != 'Y':
			return ans

	for i in range(4):
		column = []
		for y in range(4):
			column.append(game[y][i])
		ans = verify(column)
		if ans != 'Y':
			return ans

	diag = []
	for i in range(4):
		diag.append(game[i][i])
	ans = verify(diag)
	if ans != 'Y':
		return ans

	diag = []
	y = 3
	for i in range(4):
		diag.append(game[i][y])
		y -= 1
	ans = verify(diag)
	if ans != 'Y':
		return ans

	return 'Y'

def draw(game):
	for line in game:
		if '.' in line:
			return False
	return True

for t in range(1, x + 1):
	game = []
	for i in range(4):
		game.append([])
		for l in f.readline():
			if not l == '\n':
				game[i].append(l)
	f.readline()

	if won(game) != 'Y':
		print 'Case #' + str(t) + ': ' +won(game) +' won'
	elif draw(game):
		print 'Case #' + str(t) + ': Draw'
	else:
		print 'Case #' + str(t) + ': Game has not completed'
	

	




