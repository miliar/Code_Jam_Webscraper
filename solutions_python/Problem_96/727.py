#!/usr/bin/python -tt

import sys
import random
import copy

def GetVariant(num):
    #print 'Search varians for ', num
    l = []
    if num % 3 == 0:
        c1 = (num / 3, num / 3, num / 3, False)
        c2 = (num / 3, num / 3 - 1, num / 3 + 1, True)
        l.append(c1)
        if (num / 3 + 1) <= 10 and (num / 3 - 1) >= 0:
            l.append(c2)
            
    if num % 3 == 1:
        c1 = (num / 3, num / 3, num / 3 + 1, False)
        c2 = (num / 3 - 1, num / 3 + 1, num / 3 + 1, True)
        l.append(c1)
        if num / 3 - 1 >= 0:
            l.append(c2)
            
    if num % 3 == 2:
        c1 = (num / 3, num / 3 + 1, num / 3 + 1, False)
        c2 = (num / 3, num / 3, num / 3 + 2, True)
        l.append(c1)
        if num / 3 + 2 <= 10:
            l.append(c2)
    #print 'res = ', l
    return l
          
  
  
def GetVariants(points):
    v = {}
    for i in range(0, len(points)):
        v[i] = GetVariant(points[i])
    return v 

def IsSurprized(v):
    return v[3]

def GetBest(v):
    return max(v[0:3])

def IsCriticalOnlySuitable(v, p):
    return GetBest(v[0]) < p and GetBest(v[1]) >= p

def IsSuitable(v, p):
    return GetBest(v[0]) >= p or GetBest(v[1]) >= p


def main():
    f = open('B-large.in')
    out = open('B-large.out', 'w')
    
    caseNum = int(f.readline())
    
    for tc in range(1, caseNum + 1):
        print 'case #', tc
        res = 0;
        
        params = f.readline().split();
        N = int(params[0])
        S = int(params[1])
        p = int(params[2])
        points = [int(x) for x in params[3:]]
        
        #print 'points  = ', points
        
        variants = GetVariants(points)
        
        maxCount = 0
        surCount = 0
        
        for i in range(0, N):
            if len(variants[i]) == 1:
                v = variants[i][0]
                if IsSurprized(v):
                    surCount += 1
                if GetBest(v) >= p:
                    maxCount += 1
                del variants[i]
        
        for i in range(0, N):
            if i in variants:
                v = variants[i]
                if IsCriticalOnlySuitable(v, p):
                    if surCount < S:
                        maxCount += 1
                        surCount += 1
                    del variants[i]
        
                    
        for i in range(0, N):
            if i in variants:
                v = variants[i]
                if IsSuitable(v, p):
                    maxCount += 1
        
        
        print 'maxCount = ', maxCount
        
        out.write('Case #'+str(tc)+': '+str(maxCount)+'\n')
    
    out.close()
    
    
    
if __name__ == '__main__':
  main()