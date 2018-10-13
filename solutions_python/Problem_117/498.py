from sys import argv


def ints(l):
    return [int(w.strip()) for w in l.strip().split()]


def transposed(matrix):
    n = len(matrix)
    m = len(matrix[0])
    return [[matrix[i][j] for i in range(n)] for j in range(m)]


def can_be_done(grid):
    # print 'grid = ', grid
    n = len(grid)
    m = len(grid[0])
    ohs = [max(r) for r in grid]
    vhs = [max(c) for c in transposed(grid)]
    # print 'transposed(grid) = ', transposed(grid)
    # print 'ohs = ', ohs
    # print 'vhs = ', vhs
    for i in range(n):
        for j in range(m):
            if grid[i][j] != min(ohs[i], vhs[j]):
                return False
    return True




in_fname = argv[1]
f = open(in_fname)

T = int(f.readline())
for it in range(T):
    N, M = ints(f.readline())
    grid = []
    for il in range(N):
        row = ints(f.readline())
        grid.append(row)
    res = can_be_done(grid)
    print 'Case #%d: %s' % (it+1, 'YES' if res else 'NO')

