def solve():

	draw = True
	game = []

	for i in range(4):
		game.append(infile.readline())
	infile.readline()

	X = [0] * 10
	O = [0] * 10

	for x in range(4):
		for y in range(4):

			current = game[x][y]
			
			if current == 'X' or current == 'T':
				X[x] += 1
				X[y+4] += 1
				if x == y: X[8] += 1
				if x+y == 3: X[9] += 1
				if X[x] == 4 or X[y+4] == 4 or X[8] == 4 or X[9] == 4:
					return "X won"

			if current == 'O' or current == 'T':
				O[x] += 1
				O[y+4] += 1
				if x == y: O[8] += 1
				if x+y == 3: O[9] += 1
				if O[x] == 4 or O[y+4] == 4 or O[8] == 4 or O[9] == 4:
					return "O won"

			if current == '.': draw = False

	return "Draw" if draw else "Game has not completed"

infile = open('A-large.in', 'r')
outfile = open('large.out', 'w')

T = int(infile.readline())

for t in range(T):
	outfile.write("Case #" + str(t+1) + ": " + solve() + "\n")
