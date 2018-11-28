import sys
from bisect import bisect
from itertools import combinations_with_replacement, product
f=open("input" if len(sys.argv)<2 else sys.argv[1])
T=int(f.readline())

def node(S):
    if not S:
        return 0
    t = {""}
    for s in S:
        for i in range(len(s)+1):
            t.add(s[:i])    
    return len(t)
        
def best(N, S):
    #print(N,S)
    C = product( *[list(range(N))]*len(S))
    m, y = 0, 0
    for c in C:
        s = 0
        a = []
        for n in range(N):
            x = node([S[i] for i in range(len(S)) if c[i]==n])
            s+=x
        if s > m:
            m = s
            y = 0
        if s == m:
            y+=1            
    return m, y

        


for t in range(1, T+1):
    M, N = list(map(int, f.readline().split()))
    S = [f.readline().strip() for m in  range(M)]
    m, y = best(N,S)
    print("Case #%d: %d %d"%(t, m, y%1000000007))
