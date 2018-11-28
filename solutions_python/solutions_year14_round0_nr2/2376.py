def solve(C, F, X):
    t = 0.0
    cps = 2.0
    p = 10000000
    while 1:
        #print t + X/cps
        if t + X/cps > p:
            return p
        p = t + X/cps
        t += C/cps
        cps += F


T = int(raw_input())
for i in range(1, T+1):
    C, F, X = map(float, raw_input().split(" "))
    ans = solve(C, F, X)
    print "Case #%d: %.7f" % (i, ans)

