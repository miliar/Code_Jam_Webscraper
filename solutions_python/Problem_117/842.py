f = open('in.txt', 'r')

num = int(f.readline())
for t in xrange(1, num+1):
	n, m = (int(x) for x in (f.readline()).split())
	n = int(n)
	m = int(m)
	
	grid = [ ]
	for y in xrange(0, n):
		grid.append([int(x) for x in (f.readline()).split()])
	
	possible = True
	
	# while grid exists
	while grid:
		# find lowest value in each row,col
		x = 0
		y = 0
		min = 101
		
		for i in xrange(0, len(grid)):
			for j in xrange(0, len(grid[i])):
				if grid[i][j] < min:
					x = j
					y = i
					min = grid[i][j]
		
		# check if row is good
		valid = True
		for j in xrange(0, len(grid[y])):
			if grid[y][j] != min:
				valid = False
				break
		
		if valid:
			# cleanse row
			grid.pop(y)
		else:
			# check if col is good
			for i in xrange(0, len(grid)):
				# print grid
				if grid[i].pop(x) != min:
					possible = False
					break;
				
		if not possible:
			break 
		
		# clean grid
		grid = filter(None, grid)
		
	print 'Case #{0}: {1}'.format(t, "YES" if possible else "NO")
	