

def winner(board, char, additions=['T']):
	""" 
	Deduces if there is a winner
	if char and additions are in a row:
		returns True
	else:
		return False
	"""
	test_case = additions + [char]
	complete = 4
	d = [True, True]
	
	for dv, row in enumerate(board):
		if not row[dv] in test_case:
			d[0] = False
		if not row[3-dv] in test_case:
			d[1] = False

		for c in row:
			if not c in test_case:
				complete -= 1
				break

	if (bool(complete) or d[0] or d[1]):
		return True

	complete = 4
	# okay now for virtcal
	for column in range(4):
		for row in board:
			if not row[column] in test_case:
				complete -= 1
				break

	return bool(complete)

def check_draw(board):
	for row in board:
		for c in row:
			if c == ".":
				return False
	return True

def game_splitter(board):
	games = {
		0:[]
	}
	pos = 0
	for row in board:
		if not row:
			pos += 1
			games[pos] = []
		else:
			games[pos].append(row)

	return games


if __name__ == "__main__":
	# Get the input data
	inp_data = open("/media/Data/Downloads/A-large.in", "r")
	inp = inp_data.readlines()[:-1]
	inp_data.close()

	inp = [i.rstrip("\n") for i in inp][1:]

	# Lets play these games!
	games = game_splitter(inp)

	for game in games:
		board = games[game]

		human_game = game + 1

		# check for a winner
		if winner(board, 'X'):
			print "Case #%s: X won" % human_game
		elif winner(board, 'O'):
			print "Case #%s: O won" % human_game

		# now check for a draw
		elif check_draw(board):
			print "Case #%s: Draw" % human_game

		# Finally it must be incompelete
		else:
			print "Case #%s: Game has not completed" % human_game  