__author__ = 'peter'
import numpy as np


def findFirstPossibleInd(s, iStart, iEnd,maxPartner):
    if iStart>iEnd:
        return None
    iMid= (iStart+iEnd)/2
    if s[iMid]<=maxPartner:
        iNew= findFirstPossibleInd(s,iStart,iMid-1,maxPartner)
        if iNew==None:
            return iMid
        else:
            return iNew
    else:
        return findFirstPossibleInd(s,iMid+1,iEnd,maxPartner)
res=[]
with open("A-large.in","r") as inF:
    t=int(inF.readline())
    for it in xrange(t):
        n,x= map(int,inF.readline().split())
        s= map(int, inF.readline().split())
        s.sort(reverse=True)
        taken=[]
        for i in xrange(n):
            taken.append(False)
        nDiscs=0
        for i in xrange(n):
            if taken[i]:
                continue
            maxPartner= x-s[i]
            iFirstPossible= findFirstPossibleInd(s,i+1,n-1,maxPartner)
            if not iFirstPossible==None:
                for j in range(iFirstPossible,n):
                    if taken[j]:
                        continue
                    else:
                        taken[i]=True
                        taken[j]=True
                        nDiscs+=1
                        break
            if not taken[i]:
                taken[i]=True
                nDiscs+=1
        res.append(nDiscs)
with open("A-large.out","w") as outF:
    for it in xrange(t):
        outF.write("Case #%d: %d\n"%(it+1,res[it]))