
class Cake(object):

	def __init__(self, rows, cols):
		self.grid = []
		self.rows = rows
		self.cols = cols

	def add_row(self, row):
		# Fill left-to-right.
		new_row = []
		last_initial = '?'
		for initial in row:
			if initial == '?':
				new_row.append(last_initial)
			else:
				new_row.append(initial)
				last_initial = initial

		# Fill right-to-left.
		if '?' in new_row and not all(c == '?' for c in new_row):
			reversed_row = list(reversed(new_row))
			q_index = reversed_row.index('?')
			for i in range(q_index, self.cols):
				reversed_row[i] = reversed_row[i-1]
			new_row = ''.join(reversed(reversed_row))

		self.grid.append(new_row)

	def fill_empty_rows(self):
		# check first row
		if self.grid[0][0] == '?':
			self.grid[0] = self.grid[1]

		# fill other rows
		for index, row in enumerate(self.grid):
			if row[0] == '?':
				self.grid[index] = self.grid[index - 1]

	def print(self):
		for row in self.grid:
			print(''.join(row))

cases = int(input())
for case in range(1, cases + 1):
	rows, cols = map(int, input().split())
	cake = Cake(rows, cols)
	for _ in range(rows):
		cake.add_row(input())
	cake.fill_empty_rows()
	print('Case #{}:'.format(case))
	cake.print()