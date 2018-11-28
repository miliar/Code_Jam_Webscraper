t = input()

from collections import defaultdict

def solve(r,c, grid):

	rows = [0]*r
	cols = [0]*c

	d = defaultdict(int)

	for i in xrange(r):
		for j in xrange(c):
			if grid[i][j] != '?':
				rows[i] = grid[i][j]
				cols[j] = grid[i][j]

	if rows.count(0) == 0: # one entry in at least all rows
		for i in xrange(r):
			for j in xrange(c):

				cell = grid[i][j]

				for x in xrange(j+1, c):
					if grid[i][x] != '?':
						break
					else:
						grid[i][x] = cell

				for x in xrange(j-1, -1, -1):
					if grid[i][x] != '?':
						break
					else:
						grid[i][x] = cell
	else:
		for i in xrange(c):
			for j in xrange(r):
				cell = grid[j][i]
				for y in xrange(j+1, r):
					if grid[y][i] != '?':
						break
					else:
						grid[y][i] = cell
				for y in xrange(j-1, -1, -1):
					if grid[y][i] != '?':
						break
					else:
						grid[y][i] = cell

	missing = []
	missing2 = []
	isR = False
	isC = False
	for i in xrange(r):
		if grid[i] == ['?']*c:
			missing.append(grid[i])
			missing2.append(i)
			isR = True

	if not isR:
		for j in xrange(c):

			col = []
			for i in xrange(r):
				col.append(grid[i][j])

			if col == ['?']*r:
				isC = True
				missing.append(col)
				missing2.append(j)

	if isR:
		for idx in xrange(len(missing2)):
			i = missing2[idx]
			found = False
			for j in xrange(i+1, c):
				if j not in missing2:
					grid[i] = grid[j]
					found = True
					break
			if not found:
				# sweep backward
				for j in xrange(i-1, -1, -1):
					if j not in missing2:
						grid[i] = grid[j]
						break
	else:

		for idx in xrange(len(missing2)):
			i = missing2[idx]
			found = False
			for j in xrange(i+1, c):
				if j not in missing2:
					for x in xrange(r):
						grid[x][i] = grid[x][j]
						found = True
					break
			if not found:
				for j in xrange(i-1, -1, -1):
					if j not in missing2:
						for x in xrange(r):
							grid[x][i] = grid[x][j]
						break
	return grid

# print solve(3,3, [list('G??'), list('?C?'), list('??J')])
# print solve(3, 4, [list('CODE'), list('????'), list('?JAM')])

for idx in xrange(1, t + 1):

	r, c = map(int, raw_input().split())

	grid = []

	for _ in xrange(r):
		grid.append(list(raw_input().strip()))

	ans = solve(r,c,grid)
	print "Case #{0}:".format(idx)
	for r in ans:
		print ''.join(r)

