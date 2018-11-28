# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 22:58:19 2017

@author: Usuario
"""

import numpy as np
import sys

f = open('B-large.in','r')
out = open('B-large.out','w')

lines = f.readlines()
numCases = int(lines[0])
del lines[0]
results = []

for it in range(numCases):
    number = lines[it].strip()
    Flag = True
    if len(number)==1:
        results.append(number)
    else:
        while(Flag):
            Flag = False
            for di in range(len(number)-1):
                if number[di+1]<number[di]:
                    newNum = number[:di] + str(int(number[di])-1) + '9'*len(number[di:-1])
                    number=str(int(newNum))
                    results.append(number)
                    Flag = True
                    break
                else:
                    continue 
            results.append(number)
    out.write('Case #' + str(it+1) +': ' + str(results[-1]) + '\n')
out.close()