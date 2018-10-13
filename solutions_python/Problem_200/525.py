#!/usr/bin/env python

def solve(N):
    def dec(S):
        return chr(ord(S) - 1)

    S = str(N)
    if len(S) == 1:
        return N        
    for i in range(1, len(S)):
        if S[i] < S[i - 1]:
            return solve(int(S[:i - 1] + dec(S[i - 1]) + '9' * (len(S) - i)))
    return N        

T = int(input().strip())
for t in range(T):
    N = int(input().strip())
    
    print ('Case #%d: %d' % (t + 1, solve(N)))
