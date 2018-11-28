#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time

def checkRow(row):
    tokens = [0,0]
    for j in range(0, 4):
        if row[j] == 'X':
            tokens[0] += 1
        elif row[j] == 'O':
            tokens[1] += 1
        if row[j] == 'T':
            tokens[0] += 1
            tokens[1] += 1
    if tokens[0] == 4:
        return 'X won'
    elif tokens[1] == 4:
        return 'O won'
    return None

def gameState(field):
    finished = True
    ''' horizontal'''
    for row in field:
        result = checkRow(row)
        if result:
            return result
            
    ''' vertical'''
    for i in range(0,4):
        row = []
        for j in range(0,4):
            row.append(field[j][i])
            if field[j][i] == '.':
                finished = False
        result = checkRow(row)
        if result:
            return result
            
    ''' diagonal'''
    row1 = []
    row2 = []
    for i in range(0,4):
        row1.append(field[i][i])
        row2.append(field[i][-i-2])
    result = checkRow(row1)
    if result:
        return result
    result = checkRow(row2)
    if result:
        return result
            
    if finished:
        return 'Draw'
    else:
        return 'Game has not completed'

startTime = time.time()
f = open(sys.argv[1])
outF = open(sys.argv[1].split('.')[0] + '.out', 'w')
lines = f.readlines()
f.close()
for i in range(0, (int(lines[0]))):
    print >> outF, 'Case #' + str(i+1) + ':', gameState(lines[i*5 + 1 : i*5 + 5])
print '%f seconds elapsed' % (time.time() - startTime)