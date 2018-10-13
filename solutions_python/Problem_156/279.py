import sys

T = int(sys.stdin.readline())

def findBest(ps, t):
    ps.sort(reverse=True)
    if ps[0] <= 3:
        return t + ps[0]
    best = t + ps[0]
    for i in range(2, (ps[0]/2)+1):
        val = findBest(ps[1:] + [i, ps[0]-i], t+1)
        if val < best:
            best = val
    # print ps, best
    return best

for i in range(T):
    D = int(sys.stdin.readline())
    ps = map(int, sys.stdin.readline().split())
    assert len(ps) == D
    print "Case #%d: %d" % (i+1, findBest(ps,0))
