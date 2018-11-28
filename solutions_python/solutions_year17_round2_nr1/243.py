def solve(d, n, ks, ss):
    time = 0.0
    for i in xrange(0, n):
        time = max(time, (d-ks[i])/float(ss[i]))
        
    return d / time

t = int(raw_input())
for i in xrange(1, t + 1):
    d, n = [int(x) for x in raw_input().split(" ")]
    ks = []
    ss = []
    for j in xrange(0, n):
        k, s = [int(x) for x in raw_input().split(" ")]
        ks.append(k)
        ss.append(s)
    print "Case #{}: {}".format(i, solve(d, n, ks, ss))
