filein = open("B-large.in", 'r')
fileout = open("output.out", 'w')

test_cases = int(filein.readline().strip())

for test_case in range(test_cases):
    N, M = filein.readline().split()
    N, M = int(N), int(M)
    
    #reading the grid as a list of strings
    grid = []
    for i in range(N):
        grid.append(filein.readline().strip().split())
    
    #converting the grid into a list of integers
    for i in range(N):
        for j in range(M):
            grid[i][j] = int(grid[i][j])
    
    result = True
    
    for i in range(N):
        for j in range(M):
            current = grid[i][j]
            row, column = True, True
            for ii in range(N):
                row = row and grid[ii][j] <= current
            for jj in range(M):
                column = column and grid[i][jj] <= current
                
            result = result and (row or column)
    
    if result == True:
        fileout.write("Case #{}: YES\n".format(test_case+1))
    else:
        fileout.write("Case #{}: NO\n".format(test_case+1))