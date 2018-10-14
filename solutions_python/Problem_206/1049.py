import sys
with open("A-large.in") as f:
    T = int(f.readline().rstrip())
    for i in range(T):
        slowestTime = 0
        D,N = map(int, f.readline().rstrip().split())
        for h in range(N):
            p,s = map(float, f.readline().rstrip().split())
            t = (D-p)/s 
            slowestTime = max(t,slowestTime)
        print "Case #%d: %f" % (i+1, D/slowestTime)
    