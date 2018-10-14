import sys

T = int(sys.stdin.readline())
for t in range(T):
    d = map(lambda x : int(x), sys.stdin.readline().split(' '))
    N = d[0]
    S = d[1]
    p = d[2]
    total = d[3:]

    # 1 is > p, 0 otherwise
    def makeSurprise(tt):
        if tt < 2: return 0
        # k, k, k-2
        # k, k-1, k-2
        # k, k-2, k-2
        k = ((tt-2) / 3) + 2
        return int(k >= p)
        
    def makeNormal(tt):
        # k, k, k
        # k, k, k-1
        # k, k-1, k-1

        k = (tt+2) / 3  # k is max
        return int(k >= p)
    
    ans = 0
    for i in range(N):
        tt = total[i]
        if makeNormal(tt) == 1:
            ans = ans + 1
        elif S > 0 and makeSurprise(tt) == 1:
            ans = ans + 1
            S = S - 1

    print "Case #%d: %d" % (t+1, ans)

