#!/usr/bin/env python

def inp():
    return [eval(x) for x in raw_input().strip().split()]

def wp(t):
    w = 0
    m = 0
    for d in t:
        if d == '1':
            m+=1
            w+=1
        elif d == '0':
            m+=1
    if m == 0:
        return 0
    else:
        return (w+0.0)/m


def calwp(tm):
    return map(wp, tm)


def calowp(tm):
    owp = []
    for i, t in enumerate(tm):
        wps = []
        for j, d in enumerate(t):
            if d != '.':
                wps.append( wp(tm[j][:i] + tm[j][i+1:]) )
        if len(wps) == 0:
            owp.append(0)
        else:
            owp.append( (sum(wps)+0.0)/len(wps) )
    return owp

def caloowp(tm, owp):
    oowp = []
    for i, t in enumerate(tm):
        owps = []
        for j, d in enumerate(t):
            if d != '.':
                owps.append(owp[j])
        if len(owps) == 0:
            oowp.append(0)
        else:
            oowp.append( (sum(owps)+0.0)/len(owps) )
    return oowp

def calpri(wp, owp, oowp):
    return 0.25*wp + 0.50 * owp + 0.25*oowp

def solve(n):
    tm = [""]*n
    for i in xrange(n):
        tm[i] = raw_input().strip()
    wp = calwp(tm)
    owp = calowp(tm)
    oowp = caloowp(tm, owp)
    pri = map(calpri, wp, owp, oowp)
    return pri

def solveCase():
    [n] = inp()
    pri =  solve(n)
    for p in pri:
        print p

def main():
    [ncase] = inp()
    for i in xrange(ncase):
        print "Case #%d:" % (i+1,)
        solveCase()

if __name__ == "__main__":
    main()

