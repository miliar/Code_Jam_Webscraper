'''input
3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
'''
T = int(input())
for t in range(T):
    R, C = map(int, input().split())
    print("Case #{}:".format(t+1))
    grid = [[c for c in input()] for x in range(R)]

    a = 0
    for row in range(R):
    	for col in range(C):
    		if grid[row][col] != '?':
    			for i in range(col+1, C):
    				if grid[row][i] == '?':
    					grid[row][i] = grid[row][col]
    				else:
    					break
    			for i in range(col-1, -1, -1):
    				if grid[row][i] == '?':
    					grid[row][i] = grid[row][col]
    				else:
    					break

    for row in range(R-1):
    	for col in range(C):
    		if grid[row][col] != '?' and grid[row+1][col] == '?':
    			grid[row+1][col] = grid[row][col]

    for row in range(R-1, -1, -1):
    	for col in range(C):
    		if grid[row][col] != '?' and grid[row-1][col] == '?':
    			grid[row-1][col] = grid[row][col]

    for r in grid:
    	print(''.join(r))
