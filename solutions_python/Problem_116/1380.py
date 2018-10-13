

def tic():
	f = open("/home/jackiebaek/codejam/test.in")
	times = -1
	lines = f.readlines()

	cases = int(lines[0])
	lines.pop(0)
	for i in range(cases):
		grid = []
		for j in range(4):
			line = lines.pop(0)
			grid.append(line[:4])
		if i != cases-1:
			lines.pop(0) # remove empty line
		print "Case #%i:" % (i+1),
		determineWinner(grid)

def determineWinner(grid):
	empty = False
	# check row
	for line in grid:
		won = checkLine(line)
		if won:
			print won+" won"
			return
	# check columns
	for i in range(4):
		row = [grid[0][i], grid[1][i],  grid[2][i], grid[3][i]]
		won = checkLine(row)
		if won:
			print won+" won"
			return	
	diagonal1 = [grid[0][0], grid[1][1], grid[2][2], grid[3][3]]
	won = checkLine(diagonal1)
	if won:
		print won+" won"
		return
	diagonal1 = [grid[3][0], grid[2][1], grid[1][2], grid[0][3]]
	won = checkLine(diagonal1)
	if won:
		print won+" won"
		return
	# check for any .
	for row in grid:
		for char in row:
			if char == ".":
				print "Game has not completed"
				return
	print "Draw"


def checkLine(li):
	curr = "."
	for square in li:
		if square  == '.':
			return False
		elif square == "T":
			continue
		elif curr == ".":
			curr = square
		elif square != curr:
			return False
	if curr == ".":
		return False
	return curr

#print checkLine("OTOX");

tic()
