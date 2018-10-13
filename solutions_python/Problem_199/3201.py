#!/usr/bin/env python2
import sys
def is_happy(X):
    for a in X:
        if a=='-':
            return False
    return True
    #return set(X)=={'+'}

def flip(X,i,K):
    r= list(X)
    for k in xrange(i,i+K):
        r[k]= '+' if X[k]=='-' else '-'
    return ''.join(r)

def sol(S,K):
    r=None
    if is_happy(S):
        return 0
    L= len(S)
    d_min= None
    Q= [ (S,1) ]
    C= set()
    U= set()
    while Q:
        (X,d) = Q.pop(0)
        if d_min is not None and d >= d_min:
            continue
        C.add(X)
        for i in xrange(len(X)-(K-1)):
            if '-' not in X[i:i+K]:
                continue
            Y= flip(X,i,K) 
            if is_happy(Y):
                d_min= d
                continue
            if Y in C:
                continue
            if Y not in U:
                U.add(Y)
                Q.append( (Y,d+1) )
    r= d_min if d_min is not None else 'IMPOSSIBLE'
    return r

if __name__=='__main__':
    T = int(raw_input())
    for i in xrange(1, T + 1):
        S,K = raw_input().split()[:2] 
        ans = sol(S,int(K))
        print("Case #{}: {}".format(i, ans))

