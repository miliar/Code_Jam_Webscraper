#!/usr/bin/python

T=int(raw_input())
for i in xrange(0,T):
    N=raw_input()

    j=len(N)
    prv=9
    while j>0:
        j = j-1
        if(int(N[j])>prv):
            N = repr( int(N) - int(N[j+1:]) -1)
            j = len(N)-1
            prv = 9
        prv = int(N[j])

    print("Case #"+repr(i+1)+": "+N)
