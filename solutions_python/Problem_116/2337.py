import os
import sys

class Grid:
	def __init__(self, grid):
		self.grid = grid
	
	def check(self, cells, player):
		cells = [x.replace('T', player) for x in cells]
		return cells.count(player) == 4

	def rows(self, n):
		return self.grid[n]

	def cols(self, n):
		return [row[n] for row in self.grid]

	def diagonals(self):
		diag_1 = [self.grid[0][0], self.grid[1][1], self.grid[2][2], self.grid[3][3]]
		diag_2 = [self.grid[3][0], self.grid[2][1], self.grid[1][2], self.grid[0][3]]

		return [diag_1, diag_2]

	def status(self):
		for x in xrange(0, 4):
			if self.check(self.rows(x), 'O'):
				return 'O won'
			if self.check(self.cols(x), 'O'):
				return 'O won'
			
			if self.check(self.rows(x), 'X'):
				return 'X won'
			if self.check(self.cols(x), 'X'):
				return 'X won'

		for d in self.diagonals():
			if self.check(d, 'X'):
				return 'X won'
			if self.check(d, 'O'):
				return 'O won'
		
		for row in self.grid:
			for cell in row:
				if cell == '.':
					return 'Game has not completed'

		return 'Draw'

if len(sys.argv)== 1:
	print 'Usage : %s <input file>' % sys.argv[0]
	sys.exit(1)

lines = [l.strip() for l in open(sys.argv[1])]
T = int(lines.pop(0))
count = 1
i = 0
grid = []

for l in lines:
	if len(l) == 0:
		g = Grid(grid)
		print 'Case #%d: %s' % (count, g.status())
		grid = []
		count += 1
		i = 0
		continue

	if count > T:
		break

	grid.append(l)

