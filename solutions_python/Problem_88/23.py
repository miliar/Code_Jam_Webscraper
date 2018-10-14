import sys

def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    filename = argv[0] if argv else 'test.in'

    with open(filename) as f:
        numCases = int(f.readline())
        for caseNo in xrange(1, numCases+1):
            R, C, D = [int(tok) for tok in f.readline().split()]
            grid = []
            for i in xrange(R):
                grid.append([int(c) for c in f.readline().strip()])
            ans = solve(R, C, D, grid)
            out = ans if ans >= 3 else 'IMPOSSIBLE'
            print 'Case #{0}: {1}'.format(caseNo, out)

def solve(R, C, D, grid):
    K = min(R, C)
    # print K
    while True:
        if K < 3:
            break
        for i in xrange(0, R-K+1):
            for j in xrange(0, C-K+1):
                c2i = 2*i + K - 1
                c2j = 2*j + K - 1
                # print i, j, c2i, c2j, K
                si = 0
                sj = 0
                for i2 in xrange(i, i+K):
                    for j2 in xrange(j, j+K):
                        if (i2 != i and i2 != i+K-1) or (j2 != j and
                                j2 != j+K-1):
                            si += (i2*2 - c2i) * grid[i2][j2]
                            sj += (j2*2 - c2j) * grid[i2][j2]
                if si == 0 and sj == 0:
                    return K
        K -= 1
    return 0


if __name__ == '__main__':
    main()
