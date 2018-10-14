def printgrid(grid):
    for i in range(len(grid)):
        print ''.join(grid[i])

def solve(casenum, I, J):
    grid = []
    for i in range(I):
        grid.append(list(infile.readline().strip()))

    for i in range(I):
        for j in range(J):
            if i > 0 and grid[i][j] == '?':
                grid[i][j] = grid[i-1][j]
    for i in range(I)[::-1]:
        for j in range(J):
            if i < I-1 and grid[i][j] == '?':
                grid[i][j] = grid[i+1][j]
    for i in range(I):
        for j in range(J):
            if j > 0 and grid[i][j] == '?':
                grid[i][j] = grid[i][j-1]
    for i in range(I):
        for j in range(J)[::-1]:
            if j < J-1 and grid[i][j] == '?':
                grid[i][j] = grid[i][j+1]
    print "Case #%d:"%casenum
    printgrid(grid)


infile = open('input.in', 'r')
T = int(infile.readline())
for t in range(1,T+1):
    I, J = map(int, infile.readline().split(' '))
    solve(t, I, J)
