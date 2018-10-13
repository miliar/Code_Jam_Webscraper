#!/usr/bin/env python

# Google code jam 2011 : Candy Splitting

import sys

def valp(l):
    s = 0
    for e in l:
        s ^= e
    return s

def vals(l):
    s = 0
    for e in l:
        s += e
    return s

def maxi(l):
    mx = l[0]
    for e in l:
        if e > mx:
            mx = e
    return mx

def result(l):
    sols = []
    def test(ls,lp,lf):
        if ls != [] and lp != [] and valp(ls) == valp(lp):
            sols.append(max(vals(ls),vals(lp)))
        else:
            for k in range(len(lf)):
                test(ls+[lp[k]],lp[:(k)]+lp[k+1:],lf[k+1:])

    test([],l,l)

    if sols == []:
        return 'NO'
    else:
        return str(maxi(sols))

    
p = int(sys.stdin.readline())
for s in range(1,p+1):
    line = sys.stdin.readline()
    n = int(line)

    l = []
    line = sys.stdin.readline()
    for i in range(n):
        val,_,line = line.partition(' ')
        l.append(int(val))

    print("Case #" + str(s) + ": " +  result(l))

