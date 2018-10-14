def fallsoff(grid,rows,cols,r,c,dir):
	if dir == '^':
		if r == 0:
			return True
		for i in range(0,r):
			if grid[i][c] != '.':
				return False
		return True
	if dir == '<':
		if c == 0:
			return True
		for i in range(0,c):
			if grid[r][i] != '.':
				return False
		return True		
	if dir == 'v':
		if r == rows-1:
			return True
		for i in range(r+1,rows):
			if grid[i][c] != '.':
				return False
		return True
	if dir == '>':
		if c == cols-1:
			return True
		for i in range(c+1,cols):
			if grid[r][i] != '.':
				return False
		return True

optionlist = ['v','^','>','<']
		
def f(grid,rows,cols):
	changecount = 0
	for i in range(0,rows):
		for j in range(0,cols):
			if grid[i][j] != '.' and fallsoff(grid,rows,cols,i,j,grid[i][j]) == True:
				if [fallsoff(grid,rows,cols,i,j,dir) for dir in optionlist] == [True,True,True,True]:
					return 'IMPOSSIBLE'
				else: 
					changecount += 1
	return changecount

import sys

with open(sys.argv[1], "r") as fileIN:
	inputLines = fileIN.readlines()

inputLines = [line.strip() for line in inputLines]	

with open(sys.argv[2], "w") as fileOUT:
	numberOfCases = int(inputLines.pop(0))
	for num in range(numberOfCases):	
		dimensions = [int(x) for x in inputLines.pop(0).rstrip().rsplit(' ')]
		rows = dimensions[0]
		cols = dimensions[1]
		grid = []
		for i in range(0,rows):
			grid.append(inputLines.pop(0).rstrip())
		fileOUT.write('Case #' + str(num+1) + ': ' + str(f(grid,rows,cols)) + '\n')