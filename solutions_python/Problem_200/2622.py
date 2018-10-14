# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 14:25:24 2017

@author: lucas
"""

import sys
import numpy as np
infile = sys.stdin

cases = [l.replace('\n','') for l in infile][1:]
cases = [np.array(list(map(int,list(x)))) for x in cases] 
caseID = 1
for case in cases:
    print('Case #{}: '.format(caseID), end='')
    caseID += 1
    #print('debug')
    #print('starting', case)
    i = 1
    
    while(i < len(case)):
        if(case[i] < case[i-1]):
            case[i:] = 9
            case[i-1] -= 1
            i -= 2
            if(i == -1):
                break
        i += 1
    x = 0 
    while(x < len(case) and case[x] == 0):
        x += 1
    case = case[x:]
    
    print("".join(map(str,list(case))))
    