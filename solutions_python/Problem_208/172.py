def solve(n, q, es, ss, ds, u, v):
    best = []

    for i in xrange(n):
        best.append(-1)

    best[n-1] = 0
 
    for i in reversed(xrange(n-1)):
        d = 0
        t = 0
        for j in xrange(i, n-1):
            d = d + ds[j]
            if d > es[i]:
                break
            t = t + (ds[j] / ss[i])
            b = t + best[j+1]
            if best[i] == -1:
                best[i] = b
            else:
                best[i] = min(best[i], b)
        
    return best[u-1]

t = int(raw_input())
for i in xrange(1, t + 1):
    n, q = [int(x) for x in raw_input().split(" ")]
    es = []
    ss = []
    ds = []
    for j in xrange(0, n):
        e, s = [int(x) for x in raw_input().split(" ")]
        es.append(e)
        ss.append(float(s))
    for j in xrange(1, n):
        d = [int(x) for x in raw_input().split(" ")][j]
        ds.append(d)
    ds.append([int(x) for x in raw_input().split(" ")][0])
    u, v = [int(x) for x in raw_input().split(" ")]
    print "Case #{}: {}".format(i, solve(n, q, es, ss, ds, u, v))
