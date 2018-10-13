#!/usr/bin/env python2
import sys
def is_ascending(d):
    L= map(int,list(str(d)))
    P= sorted(L)
    for i in xrange(len(L)):
        if L[i]!=P[i]:
            return False
    return True
    
def sol(d):
    x= str(d)
    n= len(x)
    if n==1:
        return d
    r= d
    while not is_ascending(r):
        L= map(int,list(str(r)))
        for i in xrange(1,n):
            if L[i-1] <= L[i]:
                continue
            L[i-1]-=1
            for j in xrange(i,n):
                L[j]=9
        while len(L) and L[0]==0:
            L.pop(0)
        t= 0
        while len(L):
            t= t*10 + L.pop(0)
        r=t
    return r

if __name__=='__main__':
    N = int(raw_input())
    for i in xrange(1, N + 1):
        T = int(raw_input())
        ans = sol(T)
        print("Case #{}: {}".format(i, ans))

