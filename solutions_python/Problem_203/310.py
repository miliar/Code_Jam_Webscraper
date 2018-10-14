# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 20:56:11 2017

@author: pellowes
"""

import numpy as np
import sys

fileIn = '/Users/pellowes/test.in'
fileIn = '/Users/pellowes/Downloads/A-small-attempt0(3).in'
fileIn = '/Users/pellowes/Downloads/A-large(3).in'
fileOut = fileIn.split('.')[0]+'.out'

f = open(fileIn,'r')
fo = open(fileOut,'w')
    
def emptyColumn(grid,col):
    for thing in grid:
        if(thing[col] != '?'):
            return False
    return True

def firstNonEmptyColumn(grid,columns):
    for i in range(0,columns):
        if not emptyColumn(grid,i):
            return i
    return -1
    
def solve(r,c,grid):
    #if there are multiple in a column, propogate down.  If a column is empty, propogate from the right
    #if rightmost is empty...
    output_grid_by_column = []
    for i in range(0,c):
        output_grid_by_column.append([])
    fnec = firstNonEmptyColumn(grid,c)
    #print(fnec)
    for i in range(0,r):
        if(grid[i][fnec]!='?'):
            cur = grid[i][fnec]
            break
    for i in range(0,r):
        if(grid[i][fnec]=='?'):
            output_grid_by_column[fnec].append(cur)
        else:
            output_grid_by_column[fnec].append(grid[i][fnec])
            cur = grid[i][fnec]
    for i in range(0,fnec):
        #print(i)
        output_grid_by_column[i] = output_grid_by_column[fnec]
    for i in range(fnec+1,c):
        #print(i)
        if(emptyColumn(grid,i)):
            output_grid_by_column[i] = output_grid_by_column[i-1]
        else:
            for j in range(0,r):
                if(grid[j][i]!='?'):
                    cur = grid[j][i]
                    break
            for j in range(0,r):
                if(grid[j][i]=='?'):
                    output_grid_by_column[i].append(cur)
                else:
                    output_grid_by_column[i].append(grid[j][i])
                    cur = grid[j][i]

    toReturn = ''    
    for i in range(0,r):
        toReturn+='\n'
        for j in range(0,c):
            toReturn+=str(output_grid_by_column[j][i])
    return toReturn

numcases = int(f.readline())
for casenum in range(1,numcases+1):
    problem = f.readline().strip().split(' ')
    r = int(problem[0])
    c = int(problem[1])
    grid = []
    for row in range(0,r):
        grid.append(f.readline().strip())
    #print('---')
    fo.write('Case #' + repr(casenum) + ': ' + solve(r,c,grid)+'\n')
    
f.close()
fo.close()