import math

def flatArea(r):
    return math.pi*(r**2)



for Pr in xrange(1, input()+1):
    N, K = [int(x) for x in raw_input().split()]
    R, H = [None]*N, [None]*N
    B = [None]*N
    for i in xrange(N):
        r, h = [int(x) for x in raw_input().split()]
        R[i], H[i] = r, h
        B[i] = 2*r*h
    S = [None]*N
    B.sort()
    B.reverse()
    for i in xrange(N):
        r, h = R[i], H[i]
        b = 2*r*h
        B.remove(b)
        s = r**2 + b
        for j in xrange(K-1):
            s += B[j]
        S[i] = s
        B.append(b)
        B.sort()
        B.reverse()
    print 'Case #%d: %f'%(Pr, math.pi * max(S))