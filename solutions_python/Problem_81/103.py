#!/usr/bin/python

from decimal import Decimal as D

l=open('A.in').read().split('\n')
l.reverse()
n=int(l.pop())
for i in xrange(n):
    m=int(l.pop())
    array=[]
    for j in xrange(m):
        array.append(list(l.pop()))
    wp=[]
    for j in xrange(m):
        q=map(D,filter(lambda x: x!='.',array[j]))
        wp+=[sum(q)/len(q)]
    owp=[]
    for j in xrange(m):
        owpp=[]
        for k in xrange(m):
            if array[j][k]=='.': continue
            q=map(D,filter(lambda x: x!='.',array[k][:j]+array[k][j+1:]))
            owpp.append(sum(q)/len(q))
        owp.append(sum(owpp)/len(owpp))
    oowp=[]
    for j in xrange(m):
        oowpp=[]
        for k in xrange(m):
            if array[j][k]=='.': continue
            oowpp.append(owp[k])
        oowp.append(sum(oowpp)/len(oowpp))
    print 'Case #'+str(i+1)+':'
    for j in xrange(m):
        print wp[j]/4+owp[j]/2+oowp[j]/4

