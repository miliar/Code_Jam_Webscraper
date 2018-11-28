from itertools import combinations

def points(n, A, B, C, D, xo, yo, M):
    X = xo
    Y = yo
    yield X, Y
    for i in range(n-1):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        yield X, Y

def ok(ts):
    a,b = zip(*ts)
    return sum(a) % 3 == 0 and sum(b) % 3 == 0

def f(trees):
    #if len(trees) < 3:
        #return 0
    #for ts in combinations(trees, 3):
    #    if ok(ts):
    #        #return f(trees-frozenset(ts)) + 1
    #return 0
    return sum(ok(ts) for ts in combinations(trees, 3))

def solve(n, A, B, C, D, xo, yo, M):
    trees = frozenset(points(n, A, B, C, D, xo, yo, M))
    return f(trees)


def main(in_, out):
    N = int(in_.next())
    for i in range(N):
        n, A, B, C, D, xo, yo, M = map(int, in_.next().split())
        print >>out, 'Case #%d: %d' % (i+1, solve(n, A, B, C, D, xo, yo, M))
        #break

if __name__ == '__main__':
    import sys
    main(sys.stdin, sys.stdout)
    #print solve(*map(int, '4 10 7 1 2 0 1 20'.split()))
