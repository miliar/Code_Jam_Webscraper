#!/usr/bin/python

import sys
import psyco
import array


def GetVector(line):
    
    c = line.split()
    
    result = []
    for n in c:
        result.append(int(n))
        
    return(result)

def calc(va, vb):
    
    sum = 0    
    for i in xrange(len(va)):
        #sum += 1
        sum += va[i]*vb[i]
        
    return(sum)

def QuickPerm(a):
    
    perm = []
    p = []
    for i in xrange(len(a)):
        p.append(i)        
    p.append(len(a))
    
    i = 1
    while(i < len(a)):
        
        p[i] -= 1
        j = i % 2 * p[i]
        tmp = a[j]
        a[j] = a[i]
        a[i] = tmp      
      
        perm.append(array.array('l', a[:]))
        
        i = 1
        while p[i] == 0:
            p[i] = i
            i += 1      
    
    return(perm)  

def Perm(va, vb):
    
    return(va.sort(), vb.sort(reverse=True))
        
        
def GetMinDotProduct(nd, va, vb):
    '''
    min = 100000000
    
    vap = QuickPerm(va)
    vbp = QuickPerm(vb)        
    
    for a in vap:
        
        for b in vbp:
            
            tmp = calc(a, b, nd)            
            if tmp <= min:
                min = tmp
    '''


    va.sort()
    vb.sort(reverse=True)
    r1 = calc(va, vb)
    
    va.sort(reverse=True)
    vb.sort()
    
    r2 = calc(va, vb)
    r = r1
    if r2 < r1:
        r = r2
    
    return(r)
    

def main():
    
    caseCount = int(sys.stdin.readline().strip())
    
    for caseNum in xrange(1, caseCount+1):        
        
        nd = int(sys.stdin.readline().strip())
        
        va = GetVector(sys.stdin.readline().strip())
        vb = GetVector(sys.stdin.readline().strip())
        
        m = GetMinDotProduct(nd, va, vb)
    
        print 'Case #%d: %d' % (caseNum, m)
    
psyco.full()
main()