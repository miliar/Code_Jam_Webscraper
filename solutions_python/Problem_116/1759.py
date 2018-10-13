
class ReadHelper(object):
	def __init__(self, file_path, output_path):
		with open(file_path, 'r') as fp:
			with open(output_path, 'w') as op:
				self.num_of_test = int(fp.readline())
				for i in xrange(self.num_of_test):
					content = ''
					for j in xrange(4):
						content += fp.readline()
					board = Board(content.strip())
					result = board.parse()
					op.write('Case #{0}: {1} won\n'.format(i+1, result)) if result == 'X' or result == 'O' else op.write('Case #{0}: {1}\n'.format(i+1, result))
					fp.readline()
		fp.close()
		op.close()


class Pin(object):
	def __init__(self, p):
		self.name = p
		self.checked_column = False
		self.checked_row = False
		self.checked_diagram = False

	def __repr__(self):
		return self.name

class Board(object):
	def __init__(self, content):
		self.m = 4
		self.n = 4
		self.matrix = []
		for row in content.split('\n'):
			lrow = []
			for el in row.strip(''):
				lrow.append(Pin(el))
			self.matrix.append(lrow)

	def __repr__(self):
		s = ''
		for row in self.matrix:
			s += ' '.join(map(str, row))
			s += '\n'
		return s

	def parse(self):
		for index_row, row in enumerate(self.matrix):
			for index_column, pin in enumerate(row):
				#check column
				current = self.get_el(index_column, index_row)
				if current.name == '.':
					continue
				if not current.checked_column:
					column = self.get_column_contains(index_column, index_row)
					diff = filter(lambda x: x.name != pin.name and x.name != 'T', column)
					if len(diff) == 0:
						return current.name
					else:
						for el in column:
							el.checked_column = True

				#check row
				if not current.checked_row:
					row = self.get_row_contains(index_column, index_row)
					diff = filter(lambda x: x.name != pin.name and x.name != 'T', row)
					if len(diff) == 0:
						return current.name
					else:
						for el in row:
							el.checked_row = True

				#check diagram
				c = (index_column, index_row)
				if c == (0, 0) or c == (3, 0):
					if not current.checked_diagram:
						diagram = self.get_diagram_contains(index_column, index_row)
						diff = filter(lambda x: x.name != pin.name and x.name != 'T', diagram)
						if len(diff) == 0:
							return current.name
						else:
							current.checked_diagram = True

		blanks = self.get_pins_of('.')
		if len(blanks) == 0:
			return 'Draw'
		else:
			return 'Game has not completed'



	def get_pins_of(self, category):
		blanks = []
		for row in self.matrix:
			blanks.extend(filter(lambda x: x.name == category, row))
		return blanks

	def get_el(self, column, row):
		if column < 0 or column >= self.m:
			raise ValueError('Row error')

		if row < 0 or row >= self.n:
			raise ValueError('Column error')

		return self.matrix[row][column]

	def get_row_contains(self, column, row):
		if column < 0 or column >= self.m:
			raise ValueError('Row error')

		if row < 0 or row >= self.n:
			raise ValueError('Column error')

		return self.matrix[row]

	def get_column_contains(self, column, row):
		if column < 0 or column >= self.m:
			raise ValueError('Row error')

		if row < 0 or row >= self.n:
			raise ValueError('Column error')
		return [e[column] for e in self.matrix]

	def get_diagram_contains(self, column, row):
		co = (column, row)
		if co != (0, 0) and co != (3, 0):
			return None

		if co == (0, 0):
			return [self.get_el(0, 0), self.get_el(1, 1), self.get_el(2, 2), self.get_el(3, 3)]
		else:
			return [self.get_el(3, 0), self.get_el(2, 1), self.get_el(1, 2), self.get_el(0, 3)] 


if __name__ == '__main__':
	r = ReadHelper('./board.txt', './board_result.txt')
