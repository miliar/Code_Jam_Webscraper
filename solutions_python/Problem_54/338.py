from numpy import *

FILE = open("B-large.in","r");

def GCD(n,m):
    while (n * m > 0):
        n -= (n/m)*m;
        if (n == 0):
            return m;
        m -= (m/n)*n;
    return n+m

def Solve(N, K):
    L = [];         m = max(K);
    for e in K:
        if (e != m):
            L.append(m-e);

#    print K,L;

    while (len(L) > 1):
        n1 = L.pop(0);
        n2 = L.pop(0);
        L.append(GCD(n1,n2));
#        print L;
    if (m%L[0] == 0):
        return 0;
    return (L[0] - (m)%L[0]);       


T = int(FILE.readline());
for k in range(T):          # Each of the N cases:
    print "Case #%d:" %(k+1),
    K = map( int, FILE.readline().split() );
    N = K[0];       K.pop(0);
#    print (N,K)#, " ", Solve(N,K);
    print Solve(N,K);
