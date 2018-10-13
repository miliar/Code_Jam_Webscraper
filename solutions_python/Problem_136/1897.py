T = int(raw_input())
for case in range(1, T+1):
    C, F, X = [float(_) for _ in raw_input().split()]
    P = 2.0
    t = 0.0
    while( X/(P+F) < (X-C)/P):
        t += C/P
        P += F
    t += X/P
    print "Case #%d: %.7f" % (case, t)

