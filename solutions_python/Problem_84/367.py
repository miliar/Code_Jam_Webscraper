def convert(grid,R,C):
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '#':
                if i < R-1 and j < C-1 and grid[i+1][j] == '#' and grid[i][j+1] == '#' and grid[i+1][j+1] == '#':
                    grid[i] = grid[i][:j] + '/\\'+ grid[i][j+2:]
                    grid[i+1] = grid[i+1][:j] + '\\/'+ grid[i+1][j+2:]
                else:
                    return 'Impossible'


    return grid


for t in range(input()):
    R,C = [int(i) for i in raw_input().split()]
    grid = {}
    for i in range(R):
        grid[i] = raw_input()

    res = 'Case #{0}:'.format(t+1)
    print res
    g = convert(grid,R,C)
    if g == 'Impossible':
        print 'Impossible'
    else:
        for i in range(R):
            print g[i]

