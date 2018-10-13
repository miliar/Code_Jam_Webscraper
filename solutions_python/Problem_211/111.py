import math
for T in range(input()):
    N,K=map(int,raw_input().split())
    U=float(raw_input())
    P=sorted(map(float,raw_input().split()))
    V=[0]*N
    for n in range(1,N):
        V[n]=V[n-1]+(P[n]-P[n-1])*n
        if V[n]>U: n=n-1; break
    if n>=N: n=N-1
    s=(U-V[n])/(n+1)+P[n]
    s=s**(n+1)
    for k in range(n+1,N):
        s=s*P[k]
    print "Case #{}: {:.6f}".format(T+1,s)
