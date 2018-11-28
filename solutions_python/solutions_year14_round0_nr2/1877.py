def solve(C, F, X):
    n = 0.0
    fcost = 0.0
    mintime = X/2.0

    while True:
        n += 1
        fcost += C/(2 + (n-1)*F)
        ntime = fcost + X/(2 + n*F)
        if ntime < mintime:
            mintime = ntime
        else:
            break

    return mintime

T = int(raw_input())

for t in xrange(T):
    tokens = raw_input().split()
    C = float(tokens[0])
    F = float(tokens[1])
    X = float(tokens[2])
    print "Case #%s: %s" % (t+1, solve(C, F, X))
