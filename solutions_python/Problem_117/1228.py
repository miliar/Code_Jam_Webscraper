T = input()

def test(grid, N, M):
    for i in xrange(N):
        for j in xrange(M):
            v = grid[i][j]
            rowmax = max(grid[i])
            colmax = max([grid[t][j] for t in xrange(N)])
            if v < rowmax and v < colmax:
                return "NO"
    return "YES"

for case in xrange(1, T + 1):
    N, M = (int(x) for x in raw_input().split())
    grid = []
    for i in xrange(N):
        grid.append([int(x) for x in raw_input().split()])
    ans = test(grid, N, M)
    print "Case #%d: %s" % (case, ans)