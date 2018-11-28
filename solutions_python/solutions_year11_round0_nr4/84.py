T = int(raw_input())

def solve(ns):
    d = 0
    for i, n in enumerate(ns):
        if i+1 != n:
            d += 1
    return d

for t in xrange(1, T+1):
    raw_input()
    ns = (int(w) for w in raw_input().split())
    solution = solve(ns)

    print 'Case #%d: %f' % (t, float(solution))
