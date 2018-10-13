import sys


def processGrid(iteration, grid, N, M, maxRow, maxCol):
	for i in range(0, N):
		for j in range(0, M):
			point = grid[i][j]
			colTrue = False
			rowTrue = False

			if point >= maxCol[j]:
				colTrue = True
			if point >= maxRow[i]:
				rowTrue = True

			if not colTrue and not rowTrue:
				return False
	return True
			



def main():
	if len(sys.argv) != 2:
		print 'specify input'
		sys.exit()
	
	f = open(sys.argv[1], 'rU')

	lines = []
	for line in f:
		lines.append(line)
	
	line = lines.pop(0)
	T = int(line)

	for i in range(1, T+1):
		line = lines.pop(0)
		splits = line.split()
		N = int(splits[0])
		M = int(splits[1])

		grid = []
		maxRow = []
		maxCol = []
		for row in range(0, N):
			line = lines.pop(0)
			grid.append(line.split())

		for row in grid:
			maxRow.append(max(row))

		for col in range(0, M):
			maxForThisColumn = 0
			for j in range(0, N):
				if maxForThisColumn < grid[j][col]:
					maxForThisColumn = grid[j][col]
			maxCol.append(maxForThisColumn)

		if processGrid(i, grid, N, M, maxRow, maxCol):
			print 'Case #%d:'%i,'YES'
		else:
			print 'Case #%d:'%i,'NO'

			





if __name__ == '__main__':
	main()
