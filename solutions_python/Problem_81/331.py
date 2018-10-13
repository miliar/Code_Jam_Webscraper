#!/usr/bin/env python

# Google code jam 2011 : RPI

import sys

f_0 = [0,1]
f_1 = [1,1]

def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a

def f_simple(p):
    if p[0] == 0:
        return [0,1]
    g = gcd(p[0], p[1])
    return [p[0]//g,p[1]//g]

def f_mult(p, q):
    if p[0]*q[0] == 0:
        return [0,1]
    out = [p[0]*q[0],p[1]*q[1]]
    return f_simple(out)

def f_sdiv(p, a):
    return f_simple([p[0], p[1]*a])

def f_add(p, q):
    if p[0] == 0:
        return q
    elif q[0] == 0:
        return p

    out = [p[0]*q[1]+q[0]*p[1],p[1]*q[1]]
    return f_simple(out)

def f_c(p):
    return p[0]/p[1]

def wp(p, idd, rm):
    total = 0
    nb = 0
    for team in range(len(p[idd])):
        if p[idd][team] == '1' and team != rm:
            total += 1 
        if p[idd][team] != '.' and team != rm:
            nb += 1
    return f_simple([total, nb])

def owp(p, idd, wp):
    total = f_0
    nb = 0
    for team in range(len(p[idd])):
        if p[idd][team] != '.' and team != idd:
            total = f_add(total, wp[team][idd])
            nb +=1
    return f_sdiv(total, nb)

def oowp(p, idd, owp):
    total = f_0
    nb = 0
    for team in range(len(p[idd])):
        if p[idd][team] != '.' and team != idd:
            total = f_add(total, owp[team])
            nb +=1
    return f_sdiv(total, nb)


def result(p):
    wps = []
    for idd in range(len(p)):
        wps.append([])
        for j in range(len(p)):
            wps[idd].append(wp(p,idd,j))

    owps = []
    for idd in range(len(p)):
        owps.append(owp(p,idd,wps))

    oowps = []
    for idd in range(len(p)):
        oowps.append(oowp(p,idd,owps))

    rpis = []
    for idd in range(len(p)):
        rpii = f_add(f_mult([1,4],wps[idd][idd]),f_mult([1,2],owps[idd]))
        rpii = f_add(rpii,f_mult([1,4],oowps[idd]))
        rpis.append(f_c(rpii))

    return rpis

p = int(sys.stdin.readline())
for s in range(1,p+1):
    line = sys.stdin.readline()
    n,_,line = line.partition(' ')
    n = int(n)
    p = []
    for i in range(n):
        line = sys.stdin.readline()
        p.append([])
        for j in range(n):
            p[i].append(line[j])

    print("Case #" + str(s) + ":")
    res = result(p)
    for i in range(len(res)):
        print(res[i])

