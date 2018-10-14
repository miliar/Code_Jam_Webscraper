def checkCharWinner(c, grid):
	for i in xrange(4):
		wonInRow = True
		wonInCol = True
		for j in xrange(4):
			if grid[i][j] != c and grid[i][j] != 'T':
				wonInRow = False
			if grid[j][i] != c and grid[i][j] != 'T':
				wonInCol = False
		if wonInRow or wonInCol:
			return True
	wonInDiag1 = True
	wonInDiag2 = True
	for i in xrange(4):
		if grid[i][i] != c and grid[i][i] != 'T':
			wonInDiag1 = False
		if grid[3 - i][i] != c and grid[3 - i][i] != 'T':
			wonInDiag2 = False
	return wonInDiag1 or wonInDiag2

def anyEmpties(grid):
	for i in xrange(4):
		for j in xrange(4):
			if grid[i][j] == '.':
				return True
	return False

f = open('input', 'r')
numTests = int(f.readline())
outputs = []
for n in range(1, numTests + 1):
	grid = [[c for c in f.readline()] for i in xrange(4)]
	newLine = f.readline()
	if checkCharWinner('X', grid) and checkCharWinner('O', grid):
		outputs += ["Case #{0}: Draw".format(n)]
		continue
	if checkCharWinner('X', grid):
		outputs += ["Case #{0}: X won".format(n)]
		continue
	if checkCharWinner('O', grid):
		outputs += ["Case #{0}: O won".format(n)]
		continue
	if anyEmpties(grid):
		outputs += ["Case #{0}: Game has not completed".format(n)]
		continue
	outputs += ["Case #{0}: Draw".format(n)]

for o in outputs:
	print o