#! /usr/bin/python
# -* coding:utf-8 -*-

import sys

input=sys.stdin.read()
inList=input.split('\n')
N=int(inList.pop(0))


def search( Qlist, s, curP ):
    val = 100000
    for i,q in enumerate(Qlist[curP:]):
        if q == s:
            val = i
            break
    return curP+val

def mostlong(Slist,Qlist,curS,curP):
    maxid  = None
    maxval = -1
    for i in range(len(Slist)):
        s = Slist[i]
        if curS == s:
            continue
        val = search( Qlist, s, curP )
        if maxval <= val:
            maxval = val
            maxid = i
    return Slist[maxid],maxval

def howmany( Slist, Qlist ):
    curP = 0
    curS = None
    ret = 0
    while 1:
        curS,curP = mostlong(Slist,Qlist,curS,curP)
        if curP >= 100000:
            break
        ret+=1
    return ret

for i in range(N):
    S = int(inList.pop(0))
    Slist = [ inList.pop(0) for j in range(S)]
    Q = int(inList.pop(0))
    Qlist = [ inList.pop(0) for j in range(Q)]
    print "Case #%d: %d"%(i+1,howmany( Slist, Qlist ))


    
