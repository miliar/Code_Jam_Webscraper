import sys


def delta(N, x, y):
    total = 0
    res = [None]
    for r in xrange(N):
        for c in xrange(N):
            if x[r][c] != y[r][c]:
                res.append("%s %d %d" % (y[r][c], r + 1, c + 1))
            if y[r][c] in ['+', 'x']:
                total += 1
            elif y[r][c] == 'o':
                total += 2
    res[0] = "%d %d" % (total, len(res) - 1)
    return '\n'.join(res)


def compute(N, x):
    y = [['.'] * N for i in xrange(N)]
    if N == 1:
        y[0][0] = 'o'
        return delta(N, x, y)
    for r in xrange(N):
        for c in xrange(N):
            y[r][c] = x[r][c]
    cx = 0
    for c in xrange(N):
        if x[0][c] in ['x', 'o']:
            cx = c
            break
    for c in xrange(N):
        y[0][c] = '+'
    y[0][cx] = 'o'
    for c in xrange(1, N - 1):
        y[N - 1][c] = '+'
    if cx == N - 1:
        y[N - 1][0] = 'x'
        cx = 0
    else:
        y[N - 1][N - 1] = 'x'
    for r in xrange(1, N - 1):
        if r <= cx:
            y[r][r - 1] = 'x'
        else:
            y[r][r] = 'x'
    return delta(N, x, y)


def parse():
    N, M = map(int, sys.stdin.readline().strip().split())
    x = [['.'] * N for i in xrange(N)]
    for i in xrange(M):
        a, r, c = sys.stdin.readline().strip().split()
        r = int(r) - 1
        c = int(c) - 1
        x[r][c] = a
    return N, x


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    T = int(sys.stdin.readline().strip())
    count = 1
    part = 0
    if len(sys.argv) == 3:
        part = int(sys.argv[1])
        count = int(sys.argv[2])
    for i in xrange(T):
        data = parse()
        if i * count >= part * T and i * count < (part + 1) * T:
            result = compute(*data)
            print "Case #%d: %s" % (i + 1, result)
