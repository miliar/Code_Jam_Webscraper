class TestCase:
	def __init__(self, lines):
		self.rows = lines
	
	def check_game(self):
		if self.player_won('X'): return 'X won'
		elif self.player_won('O'): return 'O won'
		elif self.not_complete(): return 'Game has not completed'
		else: return 'Draw'
	
	def player_won(self, player):
		for i in range(4):
			if self.player_won_in_row_or_column(player, i): return True
		return self.player_won_in_diagonals(player)

	def player_won_in_row_or_column(self, player, i):
		return self.player_won_in_line(self.rows[i], player) or self.player_won_in_line(self.column(i), player)
	
	def player_won_in_diagonals(self, player):
		return self.player_won_in_line(self.diagonal_right(), player) or self.player_won_in_line(self.diagonal_left(), player)
	
	def player_won_in_line(self, line, player):
		return (line.count(player) == 3 and 'T' in line) or line.count(player) == 4
	
	def column(self, column):
		return [self.rows[0][column],
				self.rows[1][column],
				self.rows[2][column],
				self.rows[3][column]]

	def diagonal_right(self):
		return [self.rows[0][0],
				self.rows[1][1],
				self.rows[2][2],
				self.rows[3][3]]

	def diagonal_left(self):
		return [self.rows[0][3],
				self.rows[1][2],
				self.rows[2][1],
				self.rows[3][0]]
	
	def not_complete(self):
		for row in self.rows:
			if '.'in row: return True
		return False

	def result_game(self, case_index):
		return 'Case #{0}: {1}\n'.format(case_index + 1, self.check_game())


def main():
	lines = filter(None, open('A-large.in').read().splitlines())
	number_of_test_cases, lines = int(lines[0]), lines[1:]
	
	output = open('output', 'w')

	for i in range(number_of_test_cases):
		test_case, lines = TestCase(lines[:4]), lines[4:]
		output.write(test_case.result_game(i))
	
	output.close()



if __name__ == "__main__":
	    main()
