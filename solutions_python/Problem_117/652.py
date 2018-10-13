for TC in range(1, input()+1    ):
    grid = []
    n, m = map(int, raw_input().split())
    for i in range(n):
        grid += [map(int, raw_input().split())]
        
    for y, row in enumerate(grid): # iterate through rows
        if len(set(row)) == 1 and row[0] == 1: # if entire row contains lowest height
            for x in range(m):
                if len(set(grid[i][x] for i in range(n))) == 1:
                    pass
                else:
                    grid[y][x] = 2
    for x in range(m):
        row = [r[x] for r in grid]
        if len(set(row)) == 1 and row[0] == 1:
            for y in range(n):
                grid[y][x] = 2
                    
    if len({e for r in grid for e in r}) == 1:
        print 'Case #%d: YES' % TC
    else:
        print 'Case #%d: NO' % TC
