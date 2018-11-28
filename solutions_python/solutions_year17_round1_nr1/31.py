def solve(r, c, grid):
	for i in range(1,r):
		for j in range(c):
			if grid[i][j] is '?':
				grid[i][j] = grid[i-1][j]
	for i in range(r-1)[::-1]:
		for j in range(c):
			if grid[i][j] is '?':
				grid[i][j] = grid[i+1][j]
	for i in range(r):
		for j in range(1,c):
			if grid[i][j] is '?':
				grid[i][j] = grid[i][j-1]
	for i in range(r):
		for j in range(c-1)[::-1]:
			if grid[i][j] is '?':
				grid[i][j] = grid[i][j+1]



	for line in grid:
		print ''.join(line)



t = int(raw_input())

for q in range(t):
	r,c = map(int, raw_input().split())
	grid = []
	for _ in range(r):
		grid.append(list(raw_input().strip()))

	print "Case #"+ str(q+1) +": "
	solve(r,c,grid)