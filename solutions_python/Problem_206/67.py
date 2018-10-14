import sys

def go(M):
    D,N = M.split()
    D = int(D)
    N = int(N)
    A = []
    for i in range(N):
        K,S = raw_input().split()
        K=int(K)
        S=int(S)
        # Compute time to reach end
        A.append(float(D-K)/S)
    t = max(A)
    return D/t

#sys.stdin=open('dataa.txt')

T=input()
for t in range(1,T+1):
    M=raw_input()
    print "Case #{}: {}".format(t,go(M))
