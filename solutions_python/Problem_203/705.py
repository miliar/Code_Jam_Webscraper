fi = open("A-large.in.txt", "r")
T = int(fi.readline().strip())

for i in range(T):
	R, C = (int(x) for x in fi.readline().strip().split())
	grid = []
	for j in range(R):
		line = fi.readline().strip()
		grid.append([])
		for k in range(C):
			grid[j].append(line[k])
	for j in range(R):
		c = '?'
		for k in range(C):
			if c == '?' and grid[j][k] == '?':
				continue
			elif c == '?' and grid[j][k] != '?':
				c = grid[j][k]
				for l in range(k):
					grid[j][l] = c
			elif c != '?' and grid[j][k] == '?':
				grid[j][k] = c
			else:
				c = grid[j][k]
	fill = False
	for j in range(R):
		if fill == False and grid[j][0] == '?':
			continue
		elif fill == False and grid[j][0] != '?':
			fill = True
			for p in range(j):
				for q in range(C):
					grid[p][q] = grid[j][q]
		elif fill and grid[j][0] == '?':
			for q in range(C):
				grid[j][q] = grid[j-1][q]
		else:
			continue

	print "Case #%d:" % (i+1)
	for j in range(R):
		print ''.join(grid[j])

fi.close()


