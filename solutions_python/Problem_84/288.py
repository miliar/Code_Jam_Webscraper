import sys

def solve(m, R, C):
    # print m
    m = map(lambda r: list(r), m)

    imp = 'Impossible'
    for r in xrange(R):
        for c in xrange(C):
            if m[r][c] == '#':
                m[r][c] = '/'
                if c + 1 >= C or m[r][c + 1] != '#':
                    return imp
                m[r][c + 1] = '\\'
                if r + 1 >= R or m[r + 1][c] != '#':
                    return imp
                m[r + 1][c] = '\\'
                if m[r + 1][c + 1] != '#':
                    return imp
                m[r + 1][c + 1] = '/'
    m = map(lambda r: ''.join(r), m)
    return '\n'.join(m)


T = int(raw_input())

for t in xrange(T):
    R, C = map(int, sys.stdin.readline().split())
    m = []
    for i in xrange(R):
        m.append(sys.stdin.readline().strip())
    print 'Case #%d:\n%s' % (t + 1, solve(m, R, C))
