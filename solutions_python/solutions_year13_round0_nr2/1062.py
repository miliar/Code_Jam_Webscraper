from ucb import interact
f = open('lawnmow.in')
num_tests = int(f.readline())
test_number = 0

def test_single_row(x,y,grid):
	val = grid[x][y]
	for i in range(len(grid)):
		if not val >= grid[i][y]:
			return False
	return True

def test_single_col(x,y,grid):
	val = grid[x][y]
	for j in range(len(grid[0])):
		if not val >= grid[x][j]:
			return False
	return True

def test_row(x,y,grid):
	val = grid[x][y]
	for i in range(len(grid)):
		if not val >= grid[i][y]:
			if test_single_col(i, y, grid):
				continue
			return False
	return True

def test_col(x,y,grid):
	val = grid[x][y]
	for j in range(len(grid[0])):
		if not val >= grid[x][j]:
			if test_single_row(x,j,grid):
				continue
			return False
	return True

def has_less_eq_neighbor(x,y,grid):
	if len(grid) == 1:
		return True
	elif len(grid[0]) == 1:
		return True
	return test_single_row(x,y,grid) or test_single_col(x,y,grid)

def scan_grid(grid):
	for x in range(len(grid)):
		for y in range(len(grid[0])):
			if not has_less_eq_neighbor(x,y,grid):
				return False
	return True

for i in range(num_tests):
	test_number += 1
	grid = []
	rowscol = f.readline().split()
	numrows = int(rowscol[0])
	numcols = int(rowscol[1])
	for i in range(numrows):
		grid.append([int(elem) for elem in f.readline().split()])

	print("Case #{0}: {1}".format(test_number, (lambda: "YES" if scan_grid(grid) else "NO")()))
