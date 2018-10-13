import sys

def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    filename = argv[0] if argv else 'test.in'

    with open(filename) as f:
        numCases = int(f.readline())
        for caseNo in xrange(1, numCases+1):
            X, S, R, t, N = [int(tok) for tok in f.readline().split()]
            ways = []
            for i in xrange(N):
                B, E, w = [int(tok) for tok in f.readline().split()]
                ways.append((B, E, w))
                
            ans = solve(X, S, R, t, ways)
            print 'Case #{0}: {1:.8f}'.format(caseNo, ans)

def solve(X, S, R, t, ways):
    wl = 0
    for B, E, w in ways:
        wl += E - B
    nwl = X - wl

    # print X, S, R, t

    ways.append((0, nwl, 0))
    ways.sort(key=lambda x: x[2])

    totalTime = 0
    # print ways
    for B, E, w in ways:
        dist = E - B
        if t > 0:
            canCover = (R+w)*t
            if canCover > dist:
                delta = dist/float(R+w)
                t -= delta
                totalTime += delta
                continue
            elif canCover == dist:
                totalTime += t
                t = 0
                continue
            else:
                t = 0
                delta = canCover/float(R+w)
                totalTime += delta
                dist -= canCover
        totalTime += dist/float(S+w) # Walk the rest of the way
    return totalTime


if __name__ == '__main__':
    main()
