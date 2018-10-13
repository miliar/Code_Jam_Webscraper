# input parsing

import sys

data = open(sys.argv[1]).read().split("\n")

cases = int(data.pop(0))

class Board:
	def __init__(self, board, height, width):
		self.board = board
		self.height = height
		self.width = width

def isAll(board, position, value):
	row, col = position
	return all(map(lambda x: x <= value, board[col])) or all(map(lambda x: x <= value, [i[row] for i in board]))

def checkvalue(board, value):
	for r in range(board.width):
		for c in range(board.height):
			if board.board[c][r] == value:
				if not isAll(board.board, (r, c), value):
					return False
	return True

for case in range(cases):
	print "Case #%d:" % (case + 1),
	height, width = map(int, data.pop(0).split())
	board = Board([map(int, data.pop(0).split()) for i in range(height)], height, width)
	order = sorted(list(set(sum(board.board, []))))
	# print order
	# skipset = [[False for i in range(width)] for i in range(height)]
	if all(map(lambda i: checkvalue(board, i), order)):
		print "YES"
	else:
		print "NO"
	# Algorithmic proposition: For each found instance of a number, a smaller number must exist on the edge.
