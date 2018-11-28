#!/usr/bin/env python
#coding=utf-8

# Last Change: 2010-05-23 02:18:03

import sys

f = file(sys.argv[1])
ncase = int(f.readline())

for nncase in range(ncase):
    (n,m) = [int(x) for x in f.readline().split()]
    #print n,k

    s = set()
    for i in range(n):
        l = f.readline().split()[0]
        nl = l.split("/")[1:]
        s.add("/".join(nl))
    #print s

    count = 0
    for i in range(m):
        l = f.readline().split()[0]
        #print l
        nl = l.split("/")[1:]
        for j in range(len(nl)):
            temp = "/".join(nl[:j+1])
            #print temp
            if temp not in s:
                #print temp
                count += 1
                s.add(temp)

    print "Case #%d: %d"%(nncase+1, count)
    
f.close()
