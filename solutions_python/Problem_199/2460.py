import numpy as np

T = int(raw_input())

def solve():
    S = len(s)

    # print s, K, S

    cnt = 0

    for ii in xrange(S-K+1):
        if s[ii] == '-':
            cnt+=1
            for jj in xrange(K):
                s[ii+jj] = '+' if s[ii+jj] == '-' else '-'

    
    if s.count('-') > 0:
        return 'IMPOSSIBLE'
    else:
        return cnt
    

for i in xrange(T):
    s, K = raw_input().split()

    K = int(K)
    s = [c for c in s]

    sol = solve()
    print "Case #%d: %s"%(i+1,sol)



