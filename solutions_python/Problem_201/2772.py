#!/usr/bin/env python
# -*- coding: utf-8 -*-
#sabu
def tidy(x,y):
    if len(x)<2:
        return x+y
    si = 0
    for i in range(1,len(x)):
        if x[i-1]>x[i]:
            si = i
            break
    if (si>0):
        return tidy(str(int(x[:si])-1),'9'*(len(y)+len(x)-si))
    return x+y

if __name__ == "__main__":
    testcases = int(input())                    #get number of tests
    for caseNr in range(1, testcases+1):        #for each testcase
        N, K = [int(x) for x in input().strip().split()]
        nopts = [N]
        while (K>1):
            N = max(nopts)    
            nopts.remove(N)
            N -= 1
            K -= 1        
            nopts += [N//2, N-N//2]
        N = max(nopts) - 1
        smax, smin = (N - N//2), N//2
        print("Case #%i: %i %i" % (caseNr, smax, smin))
        
        