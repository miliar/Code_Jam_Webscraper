
import sys

# 0   1   2     3
# 4   5   6     7
# 8   9   (10)  (11)
# (12)(13)(14)  (15)

#rows
ITERATE = [[0,1,2,3],
	[4,5,6,7],
	[8,9,10,11],
	[12,13,14,15],
	[0,4,8,12],
	[1,5,9,13],
	[2,6,10,14],
	[3,7,11,15],
	[0,5,10,15],
	[3,6,9,12]]


class Board:
	def __init__(self,b):
		self.board = b

	def solve(self):

		condition = ""

		solution = 0
		winner = False
		hasT = False
		hasMove = False

		for LINE in ITERATE:
			solution = 0
			hasT = False
			for i in LINE:
				char = self.board[i]
				if char == ".":
					hasMove = True
					continue
				elif char == "T":
					hasT = True
				elif char == "X":
					solution += 1
				elif char == "O":
					solution -= 1

			if hasT:
				if abs(solution) == 3:
					winner = 1
					break
			else:
				if abs(solution) == 4:
					winner = 1
					break

		if winner:
			if solution > 0:
				condition = "X won"
			else:
				condition = "O won"
		else:
			if hasMove:
				condition = "Game has not completed"
			else:
				condition = "Draw"

		return condition

def parse():
	file_input = sys.stdin.readlines()

	cases = eval(file_input.pop(0))
	for case in range(0,cases):
		b = []
		for j in range(0,5):
			b += list(file_input[5*case+j].strip())
		board = Board(b)
		print "Case #{0}: {1}".format((case+1),board.solve())

def main():
	parse()

if __name__ == '__main__':
	main()
