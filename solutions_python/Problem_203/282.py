import math
import random


def solve(numRows, numCols, grid):

	emptyRow = False
	for i in range(numRows):
		if (grid[i].count("?") == numCols):
			emptyRow = True

	emptyCol = False
	for j in range(numCols):
		maybeEmptyCol = True
		for i in range(numRows):
			if grid[i][j] != "?":
				maybeEmptyCol = False
		emptyCol |= maybeEmptyCol

	if not emptyRow or (emptyRow and emptyCol):
		for i in range(numRows):
			curChar = "?"
			for j in range(numCols):
				if grid[i][j] != "?":
					curChar = grid[i][j]
					break
			for j in range(numCols):
				if grid[i][j] != "?":
					curChar = grid[i][j]
				else:
					grid[i][j] = curChar

	if emptyRow:
		for j in range(numCols):
			curChar = ""
			for i in range(numRows):
				if grid[i][j] != "?":
					curChar = grid[i][j]
					break
			for i in range(numRows):
				if grid[i][j] != "?":
					curChar = grid[i][j]
				else:
					grid[i][j] = curChar


	return map("".join, grid)




name = "A-large"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = fi.readline().strip().split(" ")
	line = map(int, line)

	grid = []
	for j in range(line[0]):
		grid.append(list(fi.readline().strip()))

	result = solve(line[0], line[1], grid)
	fout.write("Case #" + str(i + 1) + ":""\n")
	print "Case #" + str(i + 1) + ":"
	for l in result:
		fout.write(l + "\n")
		print l

fi.close()
fout.close()