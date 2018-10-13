import sys
import math
import copy
T = int(sys.stdin.readline())

def main():
	for case in range(1,T+1):
		res = solve(case)
		sys.stdout.write("Case #{}: \n{}\n".format(case, res));

def solve(case):
	global numberSpaces, numberClicked, R, C
	numbers = map(int, sys.stdin.readline().split())
	R = numbers[0]
	C = numbers[1]
	numberMines = numbers[2]

	numberSpaces = R*C-numberMines;
	numberClicked = 0

	initGrid = []
	for i in range (0, R):
			initGrid.append([])
			for j in range (0, C):
				initGrid[i].append(None)

	if numberSpaces == 1 :
			grid = copy.deepcopy(initGrid)
			grid[0][0] = 'c'
			return 	drawGrid(grid)
	else:
		for i in range (0, R):
			for j in range (0, C):
				grid = copy.deepcopy(initGrid)
				numberClicked = 1
				grid[i][j] = 'c'
				resGrid = click(grid, i, j, 'c')
				if resGrid != None:
					return 	drawGrid(resGrid)
					break
	return "Impossible"


def click(grid, i, j, value):
	global numberSpaces, numberClicked
	nhFree = getNeighbords(grid,i,j)
	
	if len(nhFree) == 0:
		return None
	if len(nhFree) > numberSpaces - numberClicked:
		return None
	else:
		for nh in nhFree:
			grid[nh[0]][nh[1]] = '.'
			numberClicked+=1

		if numberClicked == numberSpaces:
			return grid

		for nh in nhFree:
			res =  click(grid, nh[0], nh[1], 0)
			if res != None:
				return res

		for nh in nhFree:
			grid[nh[0]][nh[1]] = None
			numberClicked-=1


def getNeighbords(grid,i,j):
	global R, C
	nhFree = []
	if i-1>=0:
		if grid[i-1][j] == None:
			nhFree.append([i-1, j])
	if i+1<R:
		if grid[i+1][j] == None:
			nhFree.append([i+1, j])
	if i-1>=0 and j-1>=0: 
		if grid[i-1][j-1] == None:
			nhFree.append([i-1, j-1])
	if i-1>=0 and j+1<C: 
		if grid[i-1][j+1] == None:
			nhFree.append([i-1, j+1])
	if i+1<R and j+1<C: 
		if grid[i+1][j+1] == None:
			nhFree.append([i+1, j+1])
	if i+1<R and j-1>=0: 
		if grid[i+1][j-1] == None:
			nhFree.append([i+1, j-1])
	if j-1>=0: 
		if grid[i][j-1] == None:
			nhFree.append([i, j-1])
	if j+1<C : 
		if grid[i][j+1] == None:
			nhFree.append([i, j+1])

	return nhFree

def drawGrid(grid):
	s = ""
	for i in range(0, R):
		if i != 0:
			s += "\n"
		for j in range (0, C):
			if grid[i][j] == None:
			 	s += "*"
			else :
				s += str(grid[i][j])

	return s

numberSpaces = None
numberClicked = None
R = None
C = None

main()
