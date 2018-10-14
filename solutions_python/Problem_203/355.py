T = int(raw_input())

for t in range(1, T+1):
    R, C = map(int, raw_input().split())
    cake = []
    for r in range(R):
        cake.append(list(raw_input()))
    # print cake
    
    dirs = (
        (0, +1),
        (0, -1),
        (+1, 0),
        (-1, 0),
    )
    for d in dirs:
        dx, dy = d
        for i in range(R):
            for j in range(C):
                if cake[i][j] == '?': # maybe no need
                    ii, jj = i, j
                    while 0 <= ii < R and 0 <= jj < C and cake[ii][jj] == '?':
                        ii += dx
                        jj += dy
                    if 0 <= ii < R and 0 <= jj < C:
                        cake[i][j] = cake[ii][jj]
    
    print 'Case #%d:' % t
    for i in range(R):
        print ''.join(cake[i])