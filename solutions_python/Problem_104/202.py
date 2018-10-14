'''
Created on May 5, 2012

@author: moatasem
'''

def isIntersected(a,b):
    isIn=False
    for i in xrange(len(a)):
        for j in xrange(len(b)):
            if(a[i]==b[j]):
                isIn=True
                break
    return isIn

import itertools
def getAllSunsets(S,n):
    all_=[]
    for i in xrange(1,n):
        all_+=(list(itertools.combinations(S, i)))
    return all_



f = open("a.in", "r")
n=int(f.readline().strip())
for o  in xrange(n):
    line=f.readline().strip()
    A=[int(p) for p in line.split(" ")]
    m=A[0]
    S=A[1:]
    g=getAllSunsets (S,m)
    h={}
    for  i in range(len(g)):
        if(h.get(sum(g[i]))==None):
            h[sum(g[i])]=[g[i]]
        else:
            h.get(sum(g[i])).append(g[i])
            
    #print h
    hk=h.keys()
    print 'Case #'+str((o+1))+": "
    for i in range(len(h.keys())):
        li=h.get(hk[i])
        if(len(li)==2 and isIntersected(li[0],li[1])==False):
            print  " ".join(str(p) for p in li[0])
            print  " ".join(str(p) for p in li[1])
            break
            
           
    #print g
    
    #res='Case #'+str((i+1))+": "
    #print res