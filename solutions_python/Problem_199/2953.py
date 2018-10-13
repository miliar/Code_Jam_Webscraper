# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import numpy as np
import sys

f = open('A-large.in','r')
out = open('A-large.out','w')

lines = f.readlines()
numCases = int(lines[0])
del lines[0]
results = []

for it in range(numCases):
    giros = 0
    line = lines[it].split()
    pancpenes = line[0]
    numPanc = []
    for p in pancpenes:
        if p == '+':
            numPanc.append(+1)
        elif p == '-':
            numPanc.append(-1)
    numPanc = np.array(numPanc)
    palazo = int(line[1])
    Flag = True
    impFlag = True
    while(Flag):
        for pi in range(len(numPanc)):
            if numPanc[pi] == -1:
                if len(numPanc)-pi < palazo:
                    results.append('IMPOSSIBLE')
                    Flag = False
                    impFlag = False
                    break
                else:
                    numPanc[pi:pi+palazo] = -numPanc[pi:pi+palazo]
                    giros += 1
            elif numPanc[pi] == 1:
                continue
        if not impFlag:
            break
        
        results.append(giros)
        Flag = False
    out.write('Case #' + str(it+1) +': ' + str(results[-1]) + '\n')
out.close()
    
    
    
    
    
    