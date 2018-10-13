# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 17:32:19 2017

@author: pellowes
"""

import numpy as np
import sys

fileIn = '/Users/pellowes/test.in'
fileIn = '/Users/pellowes/Downloads/D-small-attempt1.in'
fileOut = fileIn.split('.')[0]+'out'

f = open(fileIn,'r')
fo = open(fileOut,'w')
    
def canDoOptimalEasy(grid):
    for i in range(0,len(grid)):
        if(grid[0][i] > 1):
            return i
    return 0
    
#def solveEasy(n,spots):
#    grid = np.zeros((n,n),dtype=np.int)
#    for spot in spots:
#        if(spot[0]=='+'):
#            grid[spot[1],spot[2]] = 1
#        elif(spot[0]=='x'):
#            grid[spot[1],spot[2]] = 2
#        elif(spot[0]=='o'):
#            grid[spot[1],spot[2]] = 3
#            
#    toAddUpdate = []
#    #we have our grid.  check if we can build an ideal grid, given preassigned top row only.  
#    #requires: o in corner only
#    badLocation = canDoOptimalEasy(grid)
#    if(badLocation==-1):
#        for i in range(0,len(grid)-1):
#            if(grid[0][i] > 1):
#                toAddUpdate.append('+ '+str(1)+' '+str())
#    #otherwise: set the diagonal shift around the o

#def rotateGrid90(oldGrid):
#    newGrid = np.zeros(oldGrid)
#    for i in range(0,len(oldGrid)):
#        for j in range(0,len(oldGrid)):
#            if(oldGrid[i,j]>0):
#                newGrid[j,len(oldGrid)-i] = oldGrid[i,j]
#    return newGrid
#
#def getGridRotations(startingGrid):
#    startingGrids = []
#    startingGrids.append(startingGrid)
#    for i in range(0,3):
#        startingGrids.append(rotateGrid90(startingGrids[i]))
#    return startingGrids
        

  
def solveHard(n,spots):
    
    rowsWithXorO = set()
    colsWithXorO = set()  
    rowMinusColWithTorO = set()
    rowPlusColWithTorO = set()
    
    total_score = 0
    
    startingGrid = np.zeros((n,n),dtype=np.int)
    for spot in spots:
        #print(spot)
        spotSplit = spot.split(' ')
        t = spotSplit[0]
        r = int(spotSplit[1])-1
        c = int(spotSplit[2])-1
        if(t=='+'):
            startingGrid[r,c] = 1
            rowMinusColWithTorO.add(r-c)
            rowPlusColWithTorO.add(r+c)
            total_score+=1
        elif(t=='x'):
            startingGrid[r,c] = 2
            rowsWithXorO.add(r)
            colsWithXorO.add(c)
            total_score+=1
        elif(t=='o'):
            startingGrid[r,c] = 3
            rowsWithXorO.add(r)
            colsWithXorO.add(c)
            rowMinusColWithTorO.add(r-c)
            rowPlusColWithTorO.add(r+c)
            total_score+=2
        else:
            raise NameError('bad character')
    
    
    #go blind - place the first row full of +, if safe.  
    #then set one to o (or put the x to o)
    #then add one x per row safely
    grid = np.array(startingGrid,dtype=np.int)
    iteration_order_plus = []
    for i in range(0,len(grid)//2+1):
        if(i not in iteration_order_plus):
            iteration_order_plus.append(int(i))
        if(len(grid)-i-1 not in iteration_order_plus):
            iteration_order_plus.append(int(len(grid)-i-1))
    for i in iteration_order_plus:
        for j in iteration_order_plus:
            if(grid[i,j] == 1 or grid[i,j]==3):#don't override existing shit...
                continue
            if(i+j in rowPlusColWithTorO or i-j in rowMinusColWithTorO):
                continue
            #add a +
            grid[i,j] += 1
            rowMinusColWithTorO.add(i-j)
            rowPlusColWithTorO.add(i+j)
            total_score+=1
    for i in range(0,len(grid)):
        for j in range(0,len(grid)):
            if(grid[i,j] == 2 or grid[i,j]==3):#don't override existing shit...
                continue
            if(i in rowsWithXorO or j in colsWithXorO):
                continue
            #add a x
            grid[i,j] += 2
            rowsWithXorO.add(i)
            colsWithXorO.add(j)
            total_score+=1
            
    changed = []        
    #we have maximized the score. Now diff
    for i in range(0,len(grid)):
        for j in range(0,len(grid)):
            if(grid[i,j]!=startingGrid[i,j]):
                if(grid[i,j] == 3):
                    changed.append('o '+str(i+1)+' '+str(j+1))
                elif(grid[i,j]==2):
                    changed.append('x '+str(i+1)+' '+str(j+1))
                elif(grid[i,j]==1):
                    changed.append('+ '+str(i+1)+' '+str(j+1))
         
    #print(grid)           
    toReturn = str(total_score)+' '+str(len(changed))
    for thing in changed:
        toReturn += '\n' + thing
    return toReturn
            

numcases = int(f.readline())
for casenum in range(1,numcases+1):
    problem = f.readline().strip().split(' ')
    n = int(problem[0])
    m = int(problem[1])
    spots = []
    for spot in range(0,m):
        spots.append(f.readline().strip())
    #print('-----')
    fo.write('Case #' + repr(casenum) + ': ' + solveHard(n,spots)+'\n')
    
f.close()
fo.close()