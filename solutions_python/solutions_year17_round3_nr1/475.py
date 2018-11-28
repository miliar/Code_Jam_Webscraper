import math
def maxarea(p):
    return max([tup[1] for tup in p])
def sol(n,k,p):
    p_sorted = sorted(p, key=lambda tup: -tup[0])
    S = p_sorted[:k]
    NS = p_sorted[k:]
    for t in NS:
        erase = None
        gain = 0
        area_diff= t[1] - maxarea(S)
        if area_diff > 0:
            for i,s in enumerate(S):
                side_diff= t[0] - s[0]
                gain_i = area_diff + side_diff
                if gain_i > gain:
                    erase = i
                    gain = i
        if erase is not None:
            del S[i]
            S.append(t)
    return math.pi*(maxarea(S) + sum([tup[0] for tup in S]))
                    

t = int(raw_input().strip())
for a0 in xrange(t):
    n, k  = map(int,raw_input().strip().split(" "))
    P = []
    for b0 in range(n):
        r, h  = map(float,raw_input().strip().split(" "))
        P.append((2*r*h,r*r))
    print "Case #%d: %.6f" % (a0+1,sol(n,k,P))
