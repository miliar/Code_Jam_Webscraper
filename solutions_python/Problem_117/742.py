import sys

n = 0

filename = sys.argv[1]

def move_horizontal(height, r, c, cols, case):
	# the stuff outside can only have smaller or equal height
	#if c == 0 or c == (cols - 1):
	#	return case[r][c] <= height
	# move left
	for t in range(c - 1, -1, -1):
		if case[r][t] > height:
			return False
	# move right
	for t in range(c + 1, cols, 1):
		if case[r][t] > height:
			return False
	#print '{0}, {1}, v={2}: horizontal'.format(r, c, case[r][c])
	return True

def move_vertical(height, r, c, rows, case):
	# the stuff outside can only have smaller or equal height
	#if r == 0 or r == (rows - 1):
	#	return case[r][c] <= height
	# move up
	for t in range(r - 1, -1, -1):
		if case[t][c] > height:
			return False
	# move down
	for t in range(r + 1, rows, 1):
		if case[t][c] > height:
			return False
	#print '{0}, {1}, v={2}: vertical'.format(r, c, case[r][c])
	return True

def process_case(rows, cols, case):
	#print 'rows:', rows, 'cols:', cols
	for r in xrange(rows):
		for c in xrange(cols):
			can_do = move_horizontal(case[r][c], r, c, cols, case) or move_vertical(case[r][c], r, c, rows, case)
			if not can_do:
				return 'NO'
	return 'YES'

with open(filename) as f:
	n = int(f.readline().strip())
	for casenum in xrange(n):
		rows, cols = map(int, f.readline().strip().split(' '))
		case = [None for r in xrange(rows)]
		for r in xrange(rows):
			case[r] = map(int, f.readline().strip().split(' '))
		print 'Case #{0}: {1}'.format(casenum + 1, process_case(rows, cols, case))
