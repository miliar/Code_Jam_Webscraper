filename = 'A-large'

def count_chars(s):
	d = {}
	for char in s:
		if char in d:
			d[char] = d[char] + 1
		else:
			d[char] = 1
	return d


class Game(object):
	def __init__(self, cells):
		self.cells = cells
		self.all_lines = []
		self.winner = None

		self.process_lines()


	def process_lines(self):
		for i in range(0, 15, 4):
			self.all_lines.append(self.cells[i:i + 4])

		for i in range(4):
			s = ''
			s = self.cells[i] + self.cells[i + 4] + self.cells[i + 8] + self.cells[i + 12]
			self.all_lines.append(s)

		i, j = 0, 3
		s1 = ''
		s1 = self.cells[i] + self.cells[i + 5] + self.cells[i + 10] + self.cells[i + 15]
		s2 = ''
		s2 = self.cells[j] + self.cells[j + 3] + self.cells[j + 6] + self.cells[j + 9]
		self.all_lines.append(s1)
		self.all_lines.append(s2)


	def complete(self):
		return not '.' in self.cells


if __name__ == "__main__":
	test_file = open(filename + '.in', 'r')
	# Code for reading from file here.
	num_games = int(test_file.readline())
	games = []
	s = ""
	for line in test_file:
		s = s + line.strip()
		if len(s) == 16:
			games.append(Game(s))
			s = ""

	# Code for processing data here.
	O_win1 = count_chars('OOOO')
	O_win2 = count_chars('OOOT')
	X_win1 = count_chars('XXXX')
	X_win2 = count_chars('XXXT')

	for game in games:
		for line in game.all_lines:
			if game.winner == None:
				d = count_chars(line)
				if d == O_win1 or d == O_win2:
					game.winner = 'O won'
				elif d == X_win1 or d == X_win2:
					game.winner = 'X won'

		if game.winner == None:
			if game.complete():
				game.winner = 'Draw'
			else:
				game.winner = 'Game has not completed'

	out_file = open(filename + '.out', 'w')
	# Code for writing to file here.
	for i in range(len(games)):
		s = 'Case #{}: {}\n'.format(i + 1, games[i].winner)
		out_file.write(s)
		print s

