#! /usr/bin/python
# -* coding:utf-8 -*-

import sys

input=sys.stdin.read()
inList=input.split('\n')
N=int(inList.pop(0))


def howmany(NaList,NbList,T):

    def readyT( a, T ):
        h,s = a.split(":")
        h = int(h)
        s = int(s)
        t = h*60+s+T
        ret = "%02d:%02d" % ( t/60,t%60)
        return ret

    eventL = []
    for s,a in NaList:
        eventL.append([s, 1,"A"])
        eventL.append([readyT(a,T), 0,"B"])
    for s,a in NbList:   
        eventL.append([s, 1,"B"])
        eventL.append([readyT(a,T), 0,"A"])
    eventL.sort()

    retA = 0
    retB = 0
    curA = 0
    curB = 0
    for ev in eventL:
        if ev[1] == 1:
            if ev[2] == "A":
                if curA == 0:
                    retA += 1
                else:
                    curA -= 1
            else:
                if curB == 0:
                    retB += 1
                else:
                    curB -= 1
        else:
            if ev[2] == "A":
                curA += 1
            else:
                curB += 1

    return retA, retB
    


for i in range(N):
    T=int(inList.pop(0))
    NA,NB = inList.pop(0).split()
    NA=int(NA)
    NB=int(NB)
    NaList = [ inList.pop(0).split() for j in range(NA)]
    NbList = [ inList.pop(0).split() for j in range(NB)]
    retA, retB = howmany( NaList, NbList, T )
    print "Case #%d: %d %d"%(i+1, retA, retB )


    
