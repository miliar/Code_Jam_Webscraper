import sys


def checkDirection(grid, N, M, num, i, j, di, dj):
    while i < N and i >= 0 and j < M and j >= 0:
        if grid[i][j] > num:
            return False
        i += di
        j += dj
    return True


def solve(grid, N, M):
    for i in xrange(0, N):
        for j in xrange(0, M):
            line = checkDirection(grid, N, M, grid[i][j], i, 0, 0, 1)  # line
            col = checkDirection(grid, N, M, grid[i][j], 0, j, 1, 0)  # col
            if (not line) and (not col):
                return 'NO'
    return 'YES'



def main(f):
    _t = int(f.readline())

    for t in xrange(0, _t):
        N, M = map(int, f.readline().split())
        grid = [map(int, f.readline().split()) for x in xrange(0, N)]
        print 'Case #%d: %s' % (t + 1, solve(grid, N, M))


if __name__ == '__main__':
    f = sys.stdin
    main(f)
