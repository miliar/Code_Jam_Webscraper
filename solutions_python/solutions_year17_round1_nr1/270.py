T =  int(raw_input())
for t in range(T):
	N, M = [int(k) for k in raw_input().split()]

	grid = []
	for i in range(N):
		grid.append(list(raw_input()))

	for i in range(N):
		for j in range(1, M):
			if grid[i][j] == '?' and grid[i][j-1]!='?':
				grid[i][j] = grid[i][j-1]
		
		for j in range(M-2, -1, -1):
			if grid[i][j] == '?' and grid[i][j+1] != '?':
				grid[i][j] = grid[i][j+1]


	#print grid	
	for i in range(1, N):
		if grid[i][0] == '?' and grid[i-1][0] != '?':
			grid[i] = grid[i-1][:]
	
	for i in range(N-2, -1, -1):
		if grid[i][0] == '?' and grid[i+1][0] != '?':
			grid[i] = grid[i+1][:]

	print "Case #%d:" % (t+1)
	for i in range(N):
		print ''.join(grid[i])
 
