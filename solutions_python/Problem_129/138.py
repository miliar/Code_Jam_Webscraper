#!/usr/bin/python3
# -*- coding: utf-8 -*-

def solve():
    n,m = map(int,input().split())
    oeps = [list(map(int,input().split())) for _ in range(m)]
    oeps.sort()
    z = [[0 for _ in range(n)] for _ in range(n)]
    res = 0
    for o,e,p in oeps:
        z[e-1][o-1]+=p
        if e!=o:
            res += p*((n+n-(e-o-1))*(e-o))//2
    stop = False
    while not stop:
        stop = True
        for i in range(n):
            #print(i,z)
            add = []
            for o in range(n):
                p = z[i][o]
                if p==0:
                    continue
                for k in range(o,i):
                    for o2 in range(n):
                        p2 = z[k][o2]
                        if p2==0:
                            continue
                        if o2<o:
                            pp = min(p,p2)
                            if (pp<=0):
                                continue
                            #print (i,k,o,o2,p)
                            z[k][o2]-= pp
                            z[k][o] += pp
                            z[i][o] -= pp
                            z[i][o2]+= pp
                            p = z[i][o]
                            stop = False
    #print(res)
    for e in range(n):
        for o in range(n):
            if e!=o:
                res -= z[e][o]*((n+n-(e-o-1))*(e-o))//2
    assert res>=0,res
    #print(res)
    #print(z)
    print(res%1000002013)

if __name__=="__main__":
    T = int(input())
    for t in range(1,T+1):
        print("Case #%d:"%t,end=' ')
        solve()

