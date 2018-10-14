import sys


def compute(R, C, x):
    for row in x:
        for i in xrange(C-2, -1, -1):
            if row[i] == '?':
                row[i] = row[i + 1]
        for i in xrange(1, C):
            if row[i] == '?':
                row[i] = row[i - 1]
    for i in xrange(R - 2, -1, -1):
        for j in xrange(C):
            if x[i][j] == '?':
                x[i][j] = x[i + 1][j]
    for i in xrange(1, R):
        for j in xrange(C):
            if x[i][j] == '?':
                x[i][j] = x[i - 1][j]
    for i in xrange(R):
        x[i] = ''.join(x[i])
    return '\n' + '\n'.join(x)


def parse():
    R, C = map(int, sys.stdin.readline().strip().split())
    x = []
    for i in xrange(R):
        x.append(list(sys.stdin.readline().strip()))
    return R, C, x


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    T = int(sys.stdin.readline().strip())
    for i in xrange(T):
        data = parse()
        result = compute(*data)
        print "Case #%d: %s" % (i + 1, result)
