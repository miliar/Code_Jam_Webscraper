#INTNOG

T = int(raw_input())
for t in xrange(T):
    R,C = map(int, raw_input().split())
    grid = []
    for r in xrange(R):
        grid.append(list(raw_input().strip()))

    # print
    print 'Case #{0}:'.format(t+1)
    # print 'cake:'
    # for r in xrange(R):
        # print ''.join(grid[r])
    points = []
    first_ch = ['?']*R
    for r in xrange(R):
        for c in xrange(C):
            if grid[r][c] != '?':
                points.append((r,c,grid[r][c]))
                if first_ch[r] == '?':
                    first_ch[r] = grid[r][c]
    # print points
    for r,c,ch in points:
        if first_ch[r] == ch:
            c = 0
        for i in xrange(c, C):
            grid[r][i] = ch
    r1 = points[0][0]
    for r in xrange(r1, R):
        if grid[r][0] != '?':
            continue
        for c in xrange(C):
            grid[r][c] = grid[r-1][c]
    if r1 > 0:
        for r in xrange(r1-1, -1, -1):
            for c in xrange(C):
                grid[r][c] = grid[r+1][c]
    # print 'answer:'
    for r in xrange(R):
        print ''.join(grid[r])
