#!/usr/bin/env python
import sys

def getMaxDivider(x,y):
    if x==0 or y==0:
        return 0
    m = x%y
    if m==0:
        return y
    else:
        return getMaxDivider(y,m)

def getOptimumAnniversary(ls):
    ls.sort()
    diff = []
    for i in range(len(ls)-1):
        d = ls[i+1]-ls[i]
        if d!=0:
            diff.append(ls[i+1]-ls[i])
    if len(diff)<=0:
        diff.append(0)
    if len(diff)==1:
        m = diff[0]
    else:
        m = getMaxDivider(diff[0],diff[1])
    for l in diff:
        m = getMaxDivider(l,m)
    #print m,ls
    if m==0:
        return 0
    else:
        return (-1*ls[0])%m

def wf(fileName,results):
    f = open(fileName,'w')
    for i,r in enumerate(results):
        f.write('Case #%d: %d\n'%(i+1,r))
    f.close()

def rf(fileName):
    f = open(fileName,'r')
    inputs = []
    n = int(f.readline())
    for i in range(n):
        l = f.readline()
        l = l.split()[1:]
        inputs.append([int(t) for t in l])
    return inputs
   
if __name__=='__main__':
    inputs = rf(sys.argv[-1])
    results = []
    for i,l in enumerate(inputs):
        r = getOptimumAnniversary(l)
        print i,r
        results.append(r)
    wf(sys.argv[-1][:-2]+'out',results)

