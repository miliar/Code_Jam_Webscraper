#!/usr/bin/env python
import numpy as np
import sys
import pdb
import math

sys.setrecursionlimit(15000)

def solve(S,X):
    S = sorted(S, reverse=True)
    disknum = 0

    while len(S)>0:
        small = S.pop()
        disknum += 1
        if len(S) == 0:
            break
        elif small + S[-1] > X:
            disknum += len(S)
            break
        else:
            target = X-small
            
            head = 0
            tail = len(S)-1
            while tail-head > 10:
                index = (head+tail)/2
                if S[index] > target:
                    head = index
                elif S[index] < target:
                    tail = index
                else:
                    break
            popindex = 0
            for i in range(head,tail+1):
                if S[i] <= target:
                    popindex = i
                    break
            S.pop(popindex)    
    
    return disknum
    
numcase = int(sys.stdin.readline())
for casenum in range(1,numcase+1):
    line = sys.stdin.readline().split()
    X = int(line[1])
    S = [int(i) for i in sys.stdin.readline().split()]
    
    print 'Case #' + repr(casenum)+': '+ str(solve(S,X))
    
