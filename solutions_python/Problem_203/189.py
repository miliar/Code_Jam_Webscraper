
numruns = int(input())
for run in range(numruns):
	print('Case #{0}: '.format(run+1))
	dat = input().split()
	R = int(dat[0])
	C = int(dat[1])
	grid = [['']*C for i in range(R)]
	for i in range(R):
		line=input()
		for j in range(C):
			grid[i][j]=line[j]
	
	for j in range(C):
		for i in range(1,R):
			if grid[i][j]=='?':
				grid[i][j]=grid[i-1][j]
		for i in range(R-2,-1,-1):
			if grid[i][j]=='?':
				grid[i][j]=grid[i+1][j]
	
	for j in range(1,C):
		for i in range(R):
			if grid[i][j]=='?':
				grid[i][j]=grid[i][j-1]
	
	for j in range(C-2,-1,-1):
		for i in range(R):
			if grid[i][j]=='?':
				grid[i][j]=grid[i][j+1]
	
	for i in grid:
		for j in i:
			print(j,end='')
		print()