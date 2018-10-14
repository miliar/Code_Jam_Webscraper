import sys

def checkRow(point, row):
	if '.' in row:
		return (False, True)
	if point == 'T':
		point = row[1]
	if point == row[1] or row[1] == 'T':
		if point == row[2] or row[2] == 'T':
			if point == row[3] or row[3] == 'T':
				return (True, False)
	return (False, False)

def checkRightDiag(point, grid):
	if grid[1][1] == '.' or grid[2][2] == '.' or grid[3][3] == '.' or point == '.':
		return (False, True)
	if point == 'T':
		point = grid[1][1]
	if point == grid[1][1] or grid[1][1] == 'T':
		if point == grid[2][2] or grid[2][2] == 'T':
			if point == grid[3][3] or grid[3][3] == 'T':
				return (True, False)
	return (False, False)

def checkLeftDiag(point, grid):
	if grid[1][2] == '.' or grid[2][1] == '.' or grid[3][0] == '.' or point == '.':
		return (False, True)
	if point == 'T':
		point = grid[1][2]
	if point == grid[1][2] or grid[1][2] == 'T':
		if point == grid[2][1] or grid[2][1] == 'T':
			if point == grid[3][0] or grid[3][0] == 'T':
				return (True, False)
	return (False, False)

def checkColumn(col, grid):
	if grid[0][col] == '.' or grid[1][col] == '.' or grid[2][col] == '.' or grid[3][col] == '.':
		return (False, True)
	point = grid[0][col]
	if point == 'T':
		point = grid[1][col]
	if point == grid[1][col] or grid[1][col] == 'T':
		if point == grid[2][col] or grid[2][col] == 'T':
			if point == grid[3][col] or grid[3][col] == 'T':
				return (True, False)
	return (False, False)

def checkCase(i, lines):
	grid = lines[0:4]
	notCompleted = False #init draw boolean each time

	#check first row
	point = grid[0][0]
	result = checkRow(point, grid[0])
	if result[0]:	
		if point == 'T':
			point = grid[0][1]
		print 'Case #%d:'%i,point,'won' 
		return
	if result[1]:
		notCompleted = True

	result = checkRightDiag(point, grid)
	if result[0]:
		if point == 'T':
			point = grid[1][1]
		print 'Case #%d:'%i,point,'won' 
		return
	if result[1]:
		notCompleted = True
	
	for col in range(0, 4):
		result = checkColumn(col, grid)
		if result[0]:
			point = grid[0][col]
			if grid[0][col] == 'T':
				point = grid[1][col]
			print 'Case #%d:'%i,point,'won' 
			return
		if result[1]:
			notCompleted = True
	

	point = grid[0][3]	
	result = checkLeftDiag(point, grid)
	if result[0]:
		if point == 'T':
			point = grid[1][2]
		print 'Case #%d:'%i,point,'won' 
		return
	if result[1]:
		notCompleted = True

	for row in range(1, 4):
		point = grid[row][0]
		result = checkRow(point, grid[row])
		if result[0]:
			if point == 'T':
				point = grid[row][1]
			print 'Case #%d:'%i,point,'won' 
			return
		if result[1]:
			notCompleted = True
	
	if not notCompleted:
		print 'Case #%d:'%i,'Draw'
	else:
		print 'Case #%d:'%i,'Game has not completed'
	return

def main():
	if len(sys.argv) != 2:
		print 'please specify input'
		sys.exit()

	f = open(sys.argv[1], 'rU')

	lines = []
	for line in f:
		lines.append(line)
	
	line = lines.pop(0)
	iterations = int(line)

	for i in range(1, iterations + 1):
		checkCase(i, lines)
		lines = lines[5:]


if __name__ == '__main__':
	main()
