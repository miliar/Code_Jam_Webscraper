#!/usr/bin/env python
# chteo@gcj09::0::C

from sys import argv

MOD = 10000

# count the number (mod 1e5) of substring S in text T using index D
# def dfs(S,T):
#     if len(S) == 0:
#         return 1
#     if len(T) == 0:
#         return 0
#     cnt = 0
#     for i in range(len(T)):
#         if S[0] == T[i]:
#             cnt  = (cnt + dfs(S[1:],T[i+1:])%MOD)%MOD
#     return cnt

def dp(S,T):
    A = [1]*(len(T)+1)
    B = [1]*(len(T)+1)
    #print S,T,A
    for i in xrange(len(S)):
        l = 0
        s = S[-i-1]
        for j in xrange(len(T)-i-1,-1,-1):
            if s == T[j]:
                l = (l+B[j+1]) % MOD
            A[j] = l
        A,B = B,A
        #print s,T[j],l,B

    return B[0]

f = open(argv[1])
N = int(f.readline().strip())
S = 'welcome to code jam'
#S = 'aabc'

# run test cases
for i in range(N):
    T  = f.readline().strip()
    #cnt = dfs(S,T)
    cnt = dp(S,T)
    print 'Case #%d: %04d' % (i+1,cnt)
    


