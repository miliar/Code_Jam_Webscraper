from sys import stdin
readline = stdin.readline

T = int(readline())
for t in xrange(1, T+1):
	R, C = map(int, readline().strip().split())
	grid = []
	for i in xrange(R):
		grid.append(list(readline().strip()))
	
	nonEmpty = []
	for i in xrange(R):
		for j in xrange(C):
			if grid[i][j] != '?':
				nonEmpty.append((i, j))
	
	nonEmpty.sort()
	
	filledrow, filledcolumn = -1, -1
	
	for kid in xrange(len(nonEmpty)):
		xlim, ylim = nonEmpty[kid]
		for i in xrange(filledrow+1, xlim+1):
			for j in xrange(filledcolumn+1, ylim+1):
				grid[i][j] = grid[xlim][ylim]
		
		if (kid == len(nonEmpty)-1) or (nonEmpty[kid+1][0] > nonEmpty[kid][0]):
			for i in xrange(filledrow+1, xlim+1):
				for j in xrange(ylim+1, C):
					grid[i][j] = grid[xlim][ylim]
			filledrow = xlim
			filledcolumn = -1
		else:
			filledcolumn = ylim
	
	for i in xrange(R):
		for j in xrange(C):
			if grid[i][j] == '?':
				grid[i][j] = grid[i-1][j]
	
	print "Case #%d:" % t
	for i in xrange(R):
		print ''.join(grid[i])
