import sys
from bisect import bisect
f=open("input" if len(sys.argv)<2 else sys.argv[1])
T=int(f.readline())

def best(X,S):
    S=sorted(S)
    #print(S)
    rtn = 0
    while S:
        a = S.pop()        
        i = bisect(S, X-a)
        if i >0:
            S=S[:i-1]+S[i:]
        rtn+=1
    return rtn
        


for t in range(1, T+1):
    N,X = tuple(map(int, f.readline().split()))
    S = list(map(int, f.readline().split()))
    
    #print(t, N, X, S)
    print("Case #%d: %d"%(t, best(X,S)))
