def solve(game):
	hasDot = False
	for t in ('X', 'O'):
		for i in range(4):
			horizontal = True
			vertical = True
			diagonal1 = not i
			diagonal2 = not i
			for j in range(4):
				horizontal &= game[i][j].replace('T', t) == t
				vertical &= game[j][i].replace('T', t) == t
				if i == 0:
					# print(game[j][j].replace('T', t))
					# print(game[j][3-j].replace('T', t))
					diagonal1 &= game[j][j].replace('T', t) == t
					diagonal2 &= game[j][3-j].replace('T', t) == t
				if t == 'X':
					hasDot |= game[i][j] == '.'
			# print(horizontal, vertical, diagonal1, diagonal2)
			if horizontal or vertical or diagonal1 or diagonal2:
				return t + ' won'

	return hasDot and 'Game has not completed' or 'Draw'

i = 1
firstLine = True
numberOfLines = 0
game = []
for line in open('A-large.in'):
	if numberOfLines > 0:
		game.append(line.strip())
	numberOfLines += 1
	if numberOfLines == 5:
		print('Case #' + str(i) + ': ' + solve(game))
		numberOfLines = 0
		i += 1
		game = []