def read_file(inputf):
	with open(inputf) as x:
		num_tests = int(x.readline())

		games = []
		for i in range(int(num_tests)):
			game = []
			for i in xrange(4):
				line = x.readline()
				game.append([])
				for j in xrange(4):
					game[i].append(line[j])
			games.append(game)

			skip = x.readline()

	return games

def test_game(game):
	#test all rows
	for i in enumerate(game):
		print 'testing row', i[0]
		result = test_sequence(game[i[0]])
		if result is not None:
			return result
	
	#test all columns
	for i in enumerate(game):
		print 'testing col', i[0]
		seq = [game[j[0]][i[0]] for j in enumerate(game)]
		result = test_sequence(seq)
		if result is not None:
			return result
	
	#test diags
	print 'testing left down diag'
	seq = [game[i][i] for i in range(4)]
	print '(', seq, ')'
	result = test_sequence(seq)
	if result is not None:
		return result

	print 'testing right down diag'
	seq = [game[3-i][i] for i in range(4)] 
	print '(', seq, ')'
	result = test_sequence(seq)
	if result is not None:
		return result

	#flatten list
	flat_game = [tile for row in game for tile in row]

	if any([(tile == '.') for tile in flat_game]):
		return None
	else:
		return 'D'

def test_sequence(seq):
	i = 0
	first_item = seq[i]
	while first_item == 'T' or first_item == '.':
		i += 1
		try:
			first_item = seq[i]
		except IndexError:
			return None
	for item in seq:
		if item != 'T' and item != first_item:
			return None
	return first_item

def print_game(g):
	for row in g:
		print row


g = read_file('A-large.in')

out = open('output.out', 'w')

for i in enumerate(g):
	print 'GAME', i[0]
	print_game(i[1])
	case_str = ''.join(['Case #', str(i[0]+1), ':'])
	case_result = test_game(g[i[0]])
	print 'testing over; returned', case_result

	if case_result == 'X' or case_result == 'O':
		result = case_result + ' won'
		case_str = ' '.join([case_str, result])
	elif case_result == 'D':
		case_str = ' '.join([case_str, 'Draw'])
	elif case_result is None:
		case_str = ' '.join([case_str, 'Game has not completed'])

	case_str = ''.join([case_str, '\n'])

	out.write(case_str)