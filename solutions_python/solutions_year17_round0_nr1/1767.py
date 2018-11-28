nc = input()

for i in xrange(1,nc+1):
	grid, k = raw_input().split(" ")
	k = int(k)
	grid = list(grid)
	count = 0
	for j in xrange(0,len(grid)-k+1):
		if grid[j] == '-':
			count+=1
			for u in xrange(j,j+k):
				if grid[u] == '-':
					grid[u] = '+'
				else:
					grid[u] = '-'

	grid = ''.join(grid)
	if grid.count('-') > 0:
		out = "IMPOSSIBLE"
	else:
		out = str(count)

	print "Case #%d: %s"%(i,out)
