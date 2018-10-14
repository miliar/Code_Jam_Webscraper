#!/usr/bin/python

def bisect(n,W):
    if(n<W):
        return 0

    h1 = n/2
    h2 = n/2-(n%2==0)
    
    n_split=1
    n_split+=bisect(h1,W)
    n_split+=bisect(h2,W)

    return n_split

T=int(raw_input())
for i in range(0,T):
    line = raw_input().split()
    R = int(line[0])
    C = int(line[1])
    W = int(line[2])

    #moves = (bisect(C,W)+W)*R
    moves = C/W 
    if(C%W==0):
        moves+=W-1
    else:
        moves+=W
    moves *= R

    print("Case #"+repr(i+1)+": "+repr(moves))
