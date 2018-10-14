#!/usr/bin/env python2
import sys

def sol(N,K): 
    def by_weight((left,right,pos)):
        return ( -min(left,right),-max(left,right),pos )
    B= [ (0,N) ] 
    A= {N}
    r= None
    for i in xrange(K):
        S= [ (i-L,(R-1)-i,i) for (L,R) in B for i in xrange(L,R) ]
        S.sort( key=by_weight )
        p= S.pop(0)
        A.add(p[2])
        r= ( max(p[:2]), min(p[:2]) )
        B= []
        j=0
        start=0
        while j<=N:
            if j in A or j==N:
                B.append( (start,j) )
                start= j+1
            j+= 1
    return r

if __name__=='__main__':
    T = int(raw_input())
    for i in xrange(1, T + 1):
        N,K = [ int(a) for a in raw_input().split() ]
        ans = sol(N,K)
        print("Case #{}: {} {}".format(i, *ans))

