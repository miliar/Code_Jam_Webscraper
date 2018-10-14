f = open("A-large.in", 'r')

num_games = int(f.readline())

games = []
for i in range(num_games):
	lines = []
	for j in range(4):
		lines.append(f.readline()[:4])
	games.append(lines)
	f.readline()



def horizontal(linenum):
	def f(g):
		dot_found = False
		all_x = True
		all_y = True
		for i in g[linenum]:
			if i == '.':
				dot_found = True
			
			if i != 'X' and i != 'T':
				all_x = False

			if i != 'O' and i != 'T':
				all_y = False

		if all_x:
			return 'X'
		elif all_y:
			return 'O'
		elif dot_found:
			return 'G'
		else:
			return 'D'

	return f

def vertical(rownum):
	def f(g):
		dot_found = False
		all_x = True
		all_y = True
		for j in range(4):
			i = g[j][rownum]
			if i == '.':
				dot_found = True
			
			if i != 'X' and i != 'T':
				all_x = False

			if i != 'O' and i != 'T':
				all_y = False

		if all_x:
			return 'X'
		elif all_y:
			return 'O'
		elif dot_found:
			return 'G'
		else:
			return 'D'

	return f


def diagonal():
	def f(g):
		dot_found = False
		all_x = True
		all_y = True
		for j in range(4):
			i = g[j][j]
			if i == '.':
				dot_found = True
			
			if i != 'X' and i != 'T':
				all_x = False

			if i != 'O' and i != 'T':
				all_y = False

		if all_x:
			return 'X'
		elif all_y:
			return 'O'
		elif dot_found:
			return 'G'
		else:
			return 'D'

	return f

def inverse_diagonal():
	def f(g):
		dot_found = False
		all_x = True
		all_y = True
		for j in range(4):
			i = g[j][3 - j]
			if i == '.':
				dot_found = True
			
			if i != 'X' and i != 'T':
				all_x = False

			if i != 'O' and i != 'T':
				all_y = False

		if all_x:
			return 'X'
		elif all_y:
			return 'O'
		elif dot_found:
			return 'G'
		else:
			return 'D'

	return f


rules = []

for i in range(4):
	rules.append(horizontal(i))
	rules.append(vertical(i))

rules.append(diagonal())
rules.append(inverse_diagonal())



def check_game(g):
	draw = True
	for r in rules:
		s = r(g)
		if s == 'X':
			return "X won"
		elif s == 'O':
			return 'O won'
		elif s == 'G':
			draw = False
	if draw:
		return 'Draw'
	else:
		return 'Game has not completed' 

for i in range(len(games)):
	print 'Case #' + str(i + 1) + ': ' + check_game(games[i])
