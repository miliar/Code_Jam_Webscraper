T = int(raw_input())
for tid in xrange(T):
    (R, C, D) = [int(x) for x in raw_input().split(' ')]
    cells = []
    for r in xrange(R):
        cells.append([int(x) for x in raw_input().rstrip()])
    K = min(R, C)
    solved = False
    for k in xrange(K, 2, -1):
        for r in xrange(0, R - k + 1):
            for c in xrange(0, C - k + 1):
                xsum = 0
                ysum = 0
                for y in xrange(k):
                    for x in xrange(k):
                        if x == 0 and y == 0: continue
                        if x == k - 1 and y == 0: continue
                        if x == 0 and y == k - 1: continue
                        if x == k - 1 and y == k - 1: continue
                        xsum += cells[y + r][x + c] * (x - (k - 1) / 2.0)
                        ysum += cells[y + r][x + c] * (y - (k - 1) / 2.0)
                if xsum == 0 and ysum == 0:
                    print "Case #%d: %d" % ((tid + 1), k)
                    solved = True
                    break
            if solved: break
        if solved: break
    if not solved:
        print "Case #%d: IMPOSSIBLE" % (tid + 1)

