#!/usr/bin/env python
import sys

def getEuros(R,k,gs):
    print 'gs',gs
    fastR = [0 for i in range(len(gs))]
    fastEuros = [0 for i in range(len(gs))]
    N = len(gs)
    euros = 0
    currentIndex = 0
    for r in range(R):
        if r!=0 and currentIndex==0:
            print 'r!=0 and ci==0'
            return R/r*euros+getEuros(R%r,k,gs)
        round = gs[currentIndex]
        firstIndex = currentIndex
        currentIndex = (currentIndex+1)%N
        while True:
            round += gs[currentIndex]
            if round>k or currentIndex==firstIndex:
                euros += round-gs[currentIndex]
                break
            else:
                currentIndex = (currentIndex+1)%N
        #print 'round:',r,euros
        fastIndex = (currentIndex-1)%N
        if fastEuros[fastIndex]!=0:
            print 'in fast',fastIndex, fastEuros[fastIndex]
            fastr = fastR[fastIndex]
            return fastEuros[fastIndex]+(R-fastr-1)/(r-fastr)*(euros-fastEuros[fastIndex])+getEuros((R-fastr-1)%(r-fastr),k,gs[currentIndex:]+gs[:currentIndex])
        print 'set fast[',fastIndex,']=',euros
        fastR[fastIndex]=r
        fastEuros[fastIndex]=euros
    return euros

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
        l = f.readline().split()
        R = int(l[0])
        k = int(l[1])
        N = int(l[2])
        l = f.readline().split()
        l = [int(g) for g in l]
        inputs.append((R,k,l))
    return inputs
  
 
if __name__=='__main__':
    inputs = rf(sys.argv[-1])
    results = []
    for i,l in enumerate(inputs):
        r = getEuros(*l)
        print i,r
        results.append(r)
    wf(sys.argv[-1][:-2]+'out',results)

