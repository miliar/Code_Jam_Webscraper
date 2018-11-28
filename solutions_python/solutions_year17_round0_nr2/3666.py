import sys
inp = sys.stdin
T = int(inp.readline().strip())
for i in xrange(T):
    N = inp.readline().strip()
    M = N
    for k in xrange(len(N)):
        x = len(N) - k - 2
        if x < 0:
            break
        p, q = int(M[x]), int(M[x+1])
        if p <= q:
            continue
        else:
            p -= 1
            M = N[0:x] + str(p) + '9' * (len(N) - x - 1)
    print 'Case #{0}: {1}'.format((i+1), long(M))
