import sys
def game_status(grid):
	blanks = False
	for row in xrange(len(grid)):
		xrow = orow = trow = 0
		xcol = ocol = tcol = 0
		for col in xrange(len(grid[row])):
			if grid[row][col] == 'X':
				xrow += 1
			elif grid[row][col] == 'O':
				orow += 1
			elif grid[row][col] == 'T':
				trow += 1
			elif grid[row][col] == '.':
				blanks = True

			if grid[col][row] == 'X':
				xcol += 1
			elif grid[col][row] == 'O':
				ocol += 1
			elif grid[col][row] == 'T':
				tcol += 1

		if xrow == 4 or xcol == 4or (xrow == 3 and trow == 1) or (xcol == 3 and tcol == 1):
			return 'X won'
		elif orow == 4 or ocol == 4 or (orow == 3 and trow == 1) or (ocol == 3 and tcol == 1):
			return 'O won'

	xdiag = odiag = tdiag = 0
	xrev = orev = trev = 0
	for i in xrange(len(grid)):
		if grid[i][i] == 'X':
			xdiag += 1
		elif grid[i][i] == 'O':
			odiag += 1
		elif grid[i][i] == 'T':
			tdiag += 1
	
		j = len(grid) - i - 1
		if grid[i][j] == 'X':
			xrev += 1
		elif grid[i][j] == 'O':
			orev += 1
		elif grid[i][j] == 'T':
			trev += 1

	if xdiag == 4 or xrev == 4or (xdiag == 3 and tdiag == 1) or (xrev == 3 and trev == 1):
		return 'X won'
	elif odiag == 4 or orev == 4 or (odiag == 3 and tdiag == 1) or (orev == 3 and trev == 1):
		return 'O won'
		
	if blanks:
		return 'Game has not completed'
	else:
		return 'Draw'

f = sys.stdin
n = int(f.readline())

for i in xrange(n): # read games
	grid = [[None for x in xrange(4)] for x in xrange(4)]
	for j in xrange(4): # read lines of grid
		line = f.readline()
		for k in xrange(4):
			grid[j][k] = line[k]

	print 'Case #' + str(i+1) + ': ' + game_status(grid)
	f.readline() #read blank line


