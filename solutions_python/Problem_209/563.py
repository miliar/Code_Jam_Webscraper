from math import pi

for t in xrange(input()):
    N, K = map(int, raw_input().split())
    P = []
    for i in xrange(N):
        R, H = map(int, raw_input().split())
        P += [(R, H, R*H)]
    
    print "Case #" + str(t+1) + ":",
    
    P.sort(reverse=1)
    m = 0
    
    for i in xrange(N - K + 1):
        a = (P[i][0]**2 + 2*P[i][2] + 2*sum(sorted([x[2] for x in P[i+1:]], reverse=1)[:K-1])) * pi
        if a > m: m = a
    
    print "%.6f" % m