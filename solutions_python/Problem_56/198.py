#!/usr/bin/env python
#coding=utf-8

# Last Change: 2010-05-22 11:35:32

import sys

def check(l,color,k):
    #print l, color
    if len([c for c in l if c is color]) >= k:
        for i in range(len(l)-k+1):
            if len([c for c in l[i:i+k] if c is color]) == k:
                return True
    return False

f = file(sys.argv[1])
ncase = int(f.readline())

for nncase in range(ncase):
    (n,k) = [int(x) for x in f.readline().split()]
    #print n,k

    a = []
    for i in range(n):
        t = list(f.readline().split()[0])
        while '.' in t:
            t.remove('.')
        t2 = t[::-1]
        t2 += '.' * (n-len(t))
        a.append(t2)
    #print a

    a2 = []
    for i in range(n):
        a2.append([x[i] for x in a])

    a3 = []
    for i in range(n-k+1):
        t = []
        for j in range(0, n-i):
            #print i+j,j
            t.append(a[i+j][j])
        #print t
        a3.append(t)
        t = []
        for j in range(n-i-1, i-1, -1):
            #print i+n-j-1,j
            t.append(a[i+j][j])
        #print t
        a3.append(t)
    #print a3


    red = False
    blue = False
    for x in a+a2+a3:
        if check(x,"R", k):
            red = True
            break
    for x in a+a2+a3:
        if check(x,"B", k):
            blue = True
            break

    if red and blue:
        print "Case #%d: %s"%(nncase+1,"Both")
    elif red:
        print "Case #%d: %s"%(nncase+1,"Red")
    elif blue:
        print "Case #%d: %s"%(nncase+1,"Blue")
    else:
        print "Case #%d: %s"%(nncase+1,"Neither")
    
f.close()
