

f = file("A-small-practice.in")
ls = f.readlines()
f.close()

def read_game(ls, i):
	matrix = ls[1+5*i - 5: 5+5*i - 5]
	matrix = map(lambda x: [c for c in x.strip()], matrix)
	return matrix

def get_winner(a, b, c, d):
	if a == b and b == c and c == d and a != ".":
		return a
	tmp = [x for x in [a, b, c, d] if x not in  ("T", ".")]
	if len(tmp) == 3 and tmp[1] == tmp[0]  and tmp[1] == tmp[2]:
		return tmp[1]

	return None


def check(matrix):
	is_done = True
	for l in matrix:
		if "." in l:
			is_done = False

	for l in matrix:
		winner = get_winner(l[0], l[1], l[2], l[3])
		if winner:
			return "%s won" % winner

	for i in range(0, 4):
		winner = get_winner(matrix[0][i], matrix[1][i], matrix[2][i], matrix[3][i])
		if winner:
			return "%s won" % winner

	winner = get_winner(matrix[0][0], matrix[1][1], matrix[2][2], matrix[3][3])
	if winner:
		return "%s won" % winner

	winner = get_winner(matrix[0][3], matrix[1][2], matrix[2][1], matrix[3][0])
	if winner:
		return "%s won" % winner

	if is_done:
		return "Draw"
	return "Game has not completed"

game_count = int(ls[0])
for i in range(1, game_count + 1):
	game = read_game(ls, i)
	# print game
	result = check(game)
	print "Case #%d: %s" % (i, result)
