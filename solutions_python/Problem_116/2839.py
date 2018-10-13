import sys


def build_sets(board):
	sets = []

	#horizontals
	sets.extend(board)

	#verticals
	row = board
	for colnum in range(4):
		sets.append("{0}{1}{2}{3}".format(row[0][colnum], row[1][colnum], row[2][colnum], row[3][colnum]))

	#diagonals
	sets.append("{0}{1}{2}{3}".format(row[0][0], row[1][1], row[2][2], row[3][3]))
	sets.append("{0}{1}{2}{3}".format(row[3][0], row[2][1], row[1][2], row[0][3]))

	sets = set(sets)
	return sets


def test_set(s):
	if s[0] == '.' or s[3] == '.':
		return (False, True, '.')

	if s[0] == 'T':
		if s[1] == s[2] == s[3]:
			if s[1] != '.':
				return (True, None, s[1])

	if s[3] == 'T':
		if s[0] == s[1] == s[2]:
			if s[0] != '.':
				return (True, None, s[0])

	if s[0] == s[1] == s[2] == s[3] and s != '....':
		return (True, None, s[0])

	if s.find(".") > -1:
		return (False, True, None)
	return (False, False, None)



boards = {}

lines = [line.strip() for line in open(sys.argv[1]).readlines()]

num = lines[0]
cur = 1
boards[cur] = []

for line in lines[1:]:
	if line == '':
		cur += 1
		boards[cur] = []
		continue

	boards[cur].append(line)

for key in boards.keys():
	board = boards[key]
	#print board
	board_sets = build_sets(board)
	game_has_empty_cells = False

	for s in board_sets:
		game_has_ended, empty_cells, winner = test_set(s)
		if game_has_ended:
			print "Case #{0}: {1} won".format(key, winner)
			break

		if not game_has_empty_cells:
			game_has_empty_cells = empty_cells

	#If we get here, no winner
	if not game_has_ended and game_has_empty_cells:
		print "Case #{0}: Game has not completed".format(key)
	elif not game_has_ended:
		print "Case #{0}: Draw".format(key)
		pass
