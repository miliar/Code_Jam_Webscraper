#!/usr/bin/env python

import sys
import pprint

def get_sink(h,w):
    global c
    m=M[h][w]
    north=M[h-1][w]
    west=M[h][w-1]
    east=M[h][w+1]
    south=M[h+1][w]
    
    mm = min(m,north,south,west,east)
    if m==mm:
        if res[h-1][w-1] == ' ':
            r= chr(c)
            c+=1
        else:
            return res[h-1][w-1]
    elif north==mm:
        r = get_sink(h-1,w)
    elif west==mm:
        r = get_sink(h,w-1)
    elif east==mm:
        r = get_sink(h,w+1)
    else: #south
        r = get_sink(h+1,w)
    res[h-1][w-1] = r
    return r

Z=[99999]
ff=sys.stdin
T=int(ff.next())


for i in range(1,T+1):
    H,W = map(int,ff.next().split())
    M = [Z+map(int,ff.next().split())+Z for h in range(H)]
    M.insert(0,Z*(W+2))
    M.append(Z*(W+2))
    res = [[' ']*W for h in range(H)]

    c=ord('a')
    for h in range(1,H+1):
        for w in range(1,W+1):
            res[h-1][w-1] = get_sink(h,w)
                
    print "Case #%s:"%i
    for r in res:
        print ' '.join(r)

    """

    c=ord('a')
    for h in range(1,H+1):
        for w in range(1,W+1):
            m=M[h][w]
            if m <= M[h-1][w] and m <= M[h][w-1] and m <= M[h][w+1] and m <= M[h+1][w]:
                res[h-1][w-1] = chr(c)
                c+=1
    done = False
    while not done:
        done = True
        for h in range(1,H+1):
            for ww in range(1,W+1):
                if res[h-1][ww-1] != ' ':
                    continue
                m=M[h][ww]
                n=M[h-1][ww]
                w=M[h][ww-1]
                e=M[h][ww+1]
                s=M[h+1][ww]
                
                mm = min(n,s,w,e)
                if n==mm:
                    res[h-1][ww-1] = res[h-2][ww-1]
                elif w==mm:
                    res[h-1][ww-1] = res[h-1][ww-2]
                elif e==mm:
                    res[h-1][ww-1] = res[h-1][ww]
                else:
                    res[h-1][ww-1] = res[h][ww-1]
                if res[h-1][ww-1] ==' ':
                    done = False

    print "Case #%s"%i
    for r in res:
        print ' '.join(r)
        """
