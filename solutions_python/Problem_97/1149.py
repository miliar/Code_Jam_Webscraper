#!/usr/bin/python

def recycled(px, py):
    x, y = str(px), str(py)
    return any(y == x[i:] + x[:i] for i in xrange(1, len(x)))

def solve_stupid(a, b):
    return sum(recycled(n, m)
        for n in xrange(int(a), int(b)+1)
            for m in xrange(n+1, int(b)+1))

solve = solve_stupid

if __name__ == '__main__':
    T = int(raw_input())
    for testid in xrange(1, T+1):
        a, b = raw_input().split()
        print "Case #%s: %s" % (testid, solve(a, b))