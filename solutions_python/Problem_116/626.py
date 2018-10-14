import sys

width = 4
height = 4

class Board:
	board = ['.' for i in range(width * height)]

	def set(self, x, y, value):
		self.board[x + y * width] = value

	def get(self, x, y):
		return self.board[x + y * width]

	def game_status(self):
		# Check for winning columns
		for i in range(width):
			colwin = True
			first = self.get(i, 0)
			for j in range(1, height):
				if self.get(i, j) == '.':
					colwin = False
					break
				if self.get(i, j) != first and self.get(i, j) != 'T':
					colwin = False
					break
			if colwin:
				return first + ' won'

		# Check for winning rows
		for i in range(height):
			rowwin = True
			first = self.get(0, i)
			for j in range(1, width):
				if self.get(j, i) == '.':
					rowwin = False
					break
				if self.get(j, i) != first and self.get(j, i) != 'T':
					rowwin = False
					break
			if rowwin:
				return first + ' won'

		first = self.get(0, 0)
		diagwin = True
		for i in range(1, width):
			if self.get(i, i) == '.':
				diagwin = False
				break
			if self.get(i, i) != first and self.get(i, i) != 'T':
				diagwin = False
				break
		if diagwin:
			return first + ' won'

		first = self.get(0, height - 1)
		diagwin = True
		for i in range(1, width):
			if self.get(i, height - i - 1) == '.':
				diagwin = False
				break
			if self.get(i, height - i - 1) != first and self.get(i, height - i - 1) != 'T':
				diagwin = False
				break
		if diagwin:
			return first + ' won'

		for i in range(width):
			for j in range(height):
				if self.get(i, j) == '.':
					return 'Game has not completed'

		return 'Draw'


def main():
	f = open(sys.argv[1], 'r')
	count = f.readline()
	for i in range(int(count)):
		b = Board()
		for y in range(height):
			line = f.readline()
			for x in range(width):
				b.set(x, y, line[x])
		f.readline()
		print 'Case #' + str(i + 1) + ': ' + b.game_status()

if __name__ == "__main__":
	main()