
def tr(g):
    return zip(*g)

def wino(r):
    r = ''.join(sorted(r))
    return r == 'OOOO' or r == 'OOOT'

def winx(r):
    r = ''.join(sorted(r))
    return r == 'XXXX' or r == 'TXXX'

def diag(g):
    return [r[i] for i,r in enumerate(g)]

def solve(g):
    rows = (g + tr(g)
        + [[r[i  ] for i,r in enumerate(g)]]
        + [[r[3-i] for i,r in enumerate(g)]]
    )

    # print rows

    if any(map(wino, rows)):
        return 'O won'

    if any(map(winx, rows)):
        return 'X won'

    if '.' in ''.join(''.join(i) for i in g):
        return 'Game has not completed'

    return 'Draw'


T = int(raw_input())
for t in xrange(T):
    g = [list(raw_input().strip()) for i in xrange(4)]
    s = solve(g)
    print 'Case #%d: %s' % (t+1, s)
    raw_input()