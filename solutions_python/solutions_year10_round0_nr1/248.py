#!/usr/bin/env python
import sys

def getStatusSmall(N, K):
    status = [0 for i in range(N)]
    for k in range(K):
        for i in range(N):
            status[i] = 1-status[i]
            if i==N-1 or status[i]==1:
                break;
    return all(status)

def wf(fileName,results):
    f = open(fileName,'w')
    for i,r in enumerate(results):
        f.write('Case #%d: %s\n'%(i+1,r))
    f.close()

def rf(fileName):
    f = open(fileName,'r')
    inputs = []
    n = int(f.readline())
    for i in range(n):
        l = f.readline()
        l = l.split()
        N=int(l[0])
        K=int(l[1])
        inputs.append((N,K))
    return inputs
   
if __name__=='__main__':
    inputs = rf(sys.argv[-1])
    results = []
    for ip in inputs:
        N=ip[0]
        K=ip[1]
        print N,K
        status = getStatusSmall(N,K)
        print status 
        if status:
            results.append('ON')
        else:
            results.append('OFF')
    wf(sys.argv[-1][:-2]+'out',results)

