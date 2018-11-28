def check_horizontal_X(grid):
	x_count = 0

	for line_num in grid:
		for pos in line_num:
			if pos == 'X' or pos == 'T':
				x_count+= 1
			else:
				x_count = 0
				break
		if x_count == 4:
			return True

		x_count = 0
		
	return False

def check_horizontal_O(grid):
	x_count = 0

	for line_num in grid:
		for pos in line_num:
			if pos == 'O' or pos == 'T':
				x_count+= 1
			else:
				x_count = 0
				break
		if x_count == 4:
			return True

		x_count = 0
		
	return False


def check_vertical_X(grid):
	x_count = 0

	for i in range(0, 4):
		for k in range(0, 4):
			if grid[k][i] == 'X' or grid[k][i] == 'T':
				x_count+= 1
			else:
				x_count = 0
				break
		if x_count == 4:
			return True

		x_count = 0
		
	return False


def check_vertical_O(grid):
	x_count = 0

	for i in range(0, 4):
		for k in range(0, 4):
			if grid[k][i] == 'O' or grid[k][i] == 'T':
				x_count+= 1
			else:
				x_count = 0
				break
		if x_count == 4:
			return True

		x_count = 0
		
	return False


def check_diagonal_X(grid):
	x_count = 0
	
	for i in range(0, 4):
		if grid[i][i] == 'X' or grid[i][i] == 'T':
			x_count+= 1
		else:
			x_count = 0
			break

	if x_count == 4:
		return True

	x_count = 0
	lower = 0
	upper = 3

	for i in range(0, 4):
		if grid[lower + i][upper - i] == 'X' or grid[lower + i][upper - i] == 'T':
			x_count+= 1
		else:
			x_count = 0
			break

	if x_count == 4:
		return True
	else:
		return False

def check_diagonal_O(grid):
	x_count = 0
	
	for i in range(0, 4):
		if grid[i][i] == 'O' or grid[i][i] == 'T':
			x_count+= 1
		else:
			x_count = 0
			break

	if x_count == 4:
		return True

	x_count = 0
	lower = 0
	upper = 3

	for i in range(0, 4):
		if grid[lower + i][upper - i] == 'O' or grid[lower + i][upper - i] == 'T':
			x_count+= 1
		else:
			x_count = 0
			break

	if x_count == 4:
		return True
	else:
		return False

def check_blank_spots(grid):
	for i in range(0, 4):
		for k in range(0, 4):
			if(grid[i][k] == '.'):
				return True


	return False


a = []
f = open("testq1.in", "r")

num_tests = f.readline()
num_tests = int(num_tests.rstrip())

for i in range(0,4):
	line = f.readline().rstrip()
	b = list(line)
	a.append(b)

if(check_vertical_X(a) or check_horizontal_X(a) or check_diagonal_X(a)):
	print "X won"
elif (check_vertical_O(a) or check_horizontal_O(a) or check_diagonal_O(a)):
	print "O won"
elif (check_blank_spots(a)):
	print "Game has not completed"
else:
	print "Draw"

a = []

for i in range(0, num_tests - 1):
	f.readline()
	for i in range(0,4):
		line = f.readline().rstrip()
		b = list(line)
		a.append(b)

	if(check_vertical_X(a) or check_horizontal_X(a) or check_diagonal_X(a)):
		print "X won"
	elif (check_vertical_O(a) or check_horizontal_O(a) or check_diagonal_O(a)):
		print "O won"
	elif (check_blank_spots(a)):
		print "Game has not completed"
	else:
		print "Draw"

	a = []




