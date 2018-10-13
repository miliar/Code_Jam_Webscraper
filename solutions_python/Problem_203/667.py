import sys
grid=[]

def printGrid(g):
	for i in range(len(g)):
		for j in range(len(g[i])):
			sys.stdout.write(g[i][j])
		sys.stdout.write("\n")


turn = int(raw_input())
for t in range(turn):
	r, c = (int(l) for l in raw_input().split(" "))
	grid = []
	for i in range(r):
		grid.append([a for a in raw_input().strip()])
	r_first_not = -1
	for x in range(r):
		ch ="?"
		prev = 0
		for y in range(c):
			if grid[x][y]!='?':
				if r_first_not == -1:
					r_first_not = x
				ch = grid[x][y]
				for _ in range(prev, y):
					grid[x][_] = ch
				prev = y+1
		if prev != c:
			for _ in range(prev, c):
				grid[x][_] = ch
		if ch == "?" and x>0:
			for _ in range(c):
				grid[x][_] = grid[x-1][_]
	if r_first_not != 0:
		for x in range(0, r_first_not):
			for _ in range(c):
				grid[x][_] = grid[r_first_not][_]
	print "Case #%d:" % (t+1)
	printGrid(grid)
