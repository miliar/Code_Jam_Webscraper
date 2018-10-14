#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time
import numpy as np

def checkRow(row, comp):
    if len(row) > 1 and max([int(row[j]) for j in range(len(row)) if j != i]) > int(comp):
        return False
    return True

def validPattern(field, width, height):
    field = np.array(field)
    for i in range(height):
        horizontal = field[i]
        for j in range(width):
            vertical = field[:,j]
            if not (checkRow(horizontal, field[i][j]) or checkRow(vertical, field[i][j])):
                return 'NO'
    return 'YES'

startTime = time.time()
f = open(sys.argv[1])
outF = open(sys.argv[1].split('.')[0] + '.out', 'w')
lines = f.readlines()
f.close()
line = 1
for i in range(0, (int(lines[0]))):
    size = lines[line].split(' ')
    height = int(size[0])
    width = int(size[1])
    
    end = line + height
    lawn = []
    for j in range(line + 1, end + 1):
        lawn.append(lines[j].replace('\n', '').split(' '))
    line = end + 1
    print >> outF, 'Case #' + str(i+1) + ':', validPattern(lawn, width, height)
print '%f seconds elapsed' % (time.time() - startTime)