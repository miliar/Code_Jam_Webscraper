import math
import random

def toStr(subs, grid):

	mods = 0
	points = 0
	for row in range(0, len(grid)):
		for col in range(0, len(grid)):
			if grid[row][col] in ["x", "+"]:
				points += 1
			elif grid[row][col] == "o":
				points += 2
			if subs[row][col] in ["x", "+", "o"]:
				mods += 1

	result = str(points) + " " + str(mods)

	for row in range(0, len(subs)):
		for col in range(0, len(subs)):
			if subs[row][col] in ["x", "+", "o"]:
				result += "\n" + subs[row][col] + " " + str(row+1) + " " + str(col+1)

	return result


def validMove(grid, row, col, sign):
	if (sign == "x" or sign == "+") and grid[row][col] != ".":
		return False

	if (sign == grid[row][col]):
		return False

	oldVal = grid[row][col]
	grid[row][col] = sign

	if sign == "x" or sign == "o":
		if grid[row].count("x") + grid[row].count("o") > 1:
			grid[row][col] = oldVal
			return False
		else:
			countOther = 0
			for i in range(0, len(grid)):
				if grid[i][col] in ["x", "o"]:
					countOther += 1
			if countOther > 1:
				grid[row][col] = oldVal
				return False

	if sign == "+" or sign == "o":

		# look left-top
		curX = col
		curY = row
		while curX > 0 and curY > 0:
			curX -= 1
			curY -= 1
			if grid[curY][curX] in ["+", "o"]:
				grid[row][col] = oldVal
				return False
		# look right-bottom
		curX = col
		curY = row
		while curX < len(grid)-1 and curY < len(grid)-1:
			curX += 1
			curY += 1
			if grid[curY][curX] in ["+", "o"]:
				grid[row][col] = oldVal
				return False
		# look right-top
		curX = col
		curY = row
		while curX < len(grid)-1 and curY > 0:
			curX += 1
			curY -= 1
			if grid[curY][curX] in ["+", "o"]:
				grid[row][col] = oldVal
				return False
		# look left-bottom
		curX = col
		curY = row
		while curX > 0 and curY < len(grid)-1:
			curX -= 1
			curY += 1
			if grid[curY][curX] in ["+", "o"]:
				grid[row][col] = oldVal
				return False
		
	return True


def solve(n, grid):

	subs = [["." for x in range(len(grid))] for x in range(len(grid))]

	for row in [0, len(grid)-1]:
		for col in range(0, len(grid)):
			if validMove(grid, row, col, "+"):
				subs[row][col] = "+"
				grid[row][col] = "+"

	for row in range(0, len(grid)):
		for col in range(0, len(grid)):
			if validMove(grid, row, col, "x"):
				subs[row][col] = "x"
				grid[row][col] = "x"

	for row in range(0, len(grid)):
		for col in range(0, len(grid)):
			if validMove(grid, row, col, "o"):
				subs[row][col] = "o"
				grid[row][col] = "o"

	return toStr(subs, grid)


name = "D-small-attempt2"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line1 = fi.readline().strip().split(" ")
	line1 = map(int, line1)

	grid = [["." for x in range(line1[0])] for x in range(line1[0])]
	for j in range(line1[1]):
		line2 = fi.readline().strip().split(" ")
		grid[int(line2[1])-1][int(line2[2])-1] = line2[0]

	result = solve(line1[0], grid)
	fout.write("Case #" + str(i + 1) + ": " + result + "\n")
	print "Case #" + str(i + 1) + ": " + result

fi.close()
fout.close()