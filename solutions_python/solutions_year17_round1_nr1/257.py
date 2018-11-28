import copy

T = input()
# print T
for cas in xrange(1, T+1):
	T -= 1
	R, C = map(int, raw_input().split())
	# print R, C
	grid = []
	for i in xrange(R):
		line = raw_input()
		grid.append(list(line))
	# print grid

	for i in xrange(R):
		cn = 0
		c = None
		for j in xrange(C):
			if grid[i][j] != '?':
				cn += 1
				c = grid[i][j]
			elif c:
				grid[i][j] = c
		if cn == 0 and i > 0:
			grid[i] = copy.deepcopy(grid[i-1])

	for i in range(R)[::-1]:
		cn = 0
		c = None
		for j in range(C)[::-1]:
			if grid[i][j] != '?':
				cn += 1
				c = grid[i][j]
			elif c:
				grid[i][j] = c
		if cn == 0 and i+1 < R:
			grid[i] = copy.deepcopy(grid[i+1])

	print "Case #%d:" % (cas)
	for i in xrange(R):
		print str(''.join(grid[i]))

















