'''
Created on Apr 14, 2012

@author: siavash
'''
import sys
from math import *
def isSurprise(p):
    if(not(abs(p[0]-p[1])<2)):return True
    elif(not(abs(p[0]-p[2])<2)):return True
    elif(not(abs(p[1]-p[2])<2)):return True
    else:return False
def toTriplets(n):
    w=n/3
    res=[]
    res.append((w,w,n-w-w))
    if(res[0][2]==res[0][1]):res.append((res[0][2]-1,res[0][0],res[0][1]+1))
    if(res[0][2]==res[0][1]+2):res.append((res[0][0],res[0][1]+1,res[0][2]-1))
    return res
def solveFor(n,s,l,javab,allj):
    if(n==0):
        #print javab
#        if(not(javab in allj)):
        allj.append(javab)
        return allj
    if(len(l)==0):
        #print javab
        return
#    for i in l:
    for j in toTriplets(l[n-1]):
        if(-1 in j):continue
        if(-2 in j):continue
        if((s!=0) and (isSurprise(j))):
            tmp=(l+[])
            tmp.remove(l[n-1])
            solveFor(n-1, s-1, tmp,javab+[j],allj)
        elif(not(isSurprise(j))):
            tmp=(l+[])
            tmp.remove(l[n-1])
            solveFor(n-1, s, tmp,javab+[j],allj)
    return allj
f=sys.stdin
n=int(f.readline())
for i in range(0,n):
    tmp=f.readline()[:-1].split(" ")
    tmp=map(int,tmp)
    qwe=solveFor(tmp[0],tmp[1],tmp[3:],[],[])
#    for k in qwe:
#        print k,tmp[2]
    mx=0
    for k in qwe:
        c=0
        for l in k:
            if(l[2]>=tmp[2]):
                c+=1
        mx=max(mx,c)
    print "Case #%d: %d"%(i+1,mx)