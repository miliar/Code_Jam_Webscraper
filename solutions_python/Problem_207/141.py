# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 11:51:25 2017

@author: pellowes
"""


import numpy as np
import sys

fileIn = '/Users/pellowes/test.in'
fileIn = '/Users/pellowes/Downloads/B-small-attempt1(1).in'
fileIn = '/Users/pellowes/Downloads/B-large(3).in'
fileOut = fileIn.split('.')[0]+'.out'

f = open(fileIn,'r')
fo = open(fileOut,'w')
    
    
def solve(n,r,o,y,g,b,v):
    #first pair up the multi colored
    #print('------')
    #print([n,r,o,y,g,b,v])
    multicolored = [o,g,v]
    single = [b,r,y]
    singleMod = [b,r,y]
    #print(multicolored)
    #print(singleMod)    
    
    multiletter = ['o','g','v']
    singleletter = ['b','r','y']
    
    order = ''
    
    for i in range(0,len(multicolored)):       
        #sandwhich them - so treat as one single to the outside
        if(multicolored[i]==0):
            continue
        if(multicolored[i] > single[i] or (multicolored[i] >= single[i] and single[i]+multicolored[i] < n)):
            return "IMPOSSIBLE"
        if(multicolored[i] >= single[i] and single[i]+multicolored[i] == n):
            simpleRepeat = ''
            for j in range(0,multicolored[i]):
                simpleRepeat+=multiletter[i]
                simpleRepeat+=singleletter[i]
            return simpleRepeat
        singleMod[i]-=multicolored[i]
        
    singleModSum = singleMod[0]+singleMod[1]+singleMod[2]
    if(singleMod[0] / singleModSum > .5):
        return "IMPOSSIBLE"
    elif(singleMod[1] / singleModSum > .5):
        return "IMPOSSIBLE"
    elif(singleMod[2] / singleModSum > .5):
        return "IMPOSSIBLE"
        
    firsts=[True,True,True]
    first = -1
    prev = -1
    while(singleModSum > 0):
        
        #print(singleMod)
        bestScore = 0
        bestIndex = -1
        for i in range(0,len(singleMod)):
            if i==prev:
                continue
            elif singleMod[i] > bestScore:
                bestIndex=i
                bestScore=singleMod[i]
            elif singleMod[i] == bestScore and i == first:
                bestIndex=i
        if(firsts[bestIndex]):
            firsts[bestIndex]=False
            for i in range(0,multicolored[bestIndex]):
                order+=singleletter[bestIndex]
                order+=multiletter[bestIndex]
        order+=singleletter[bestIndex]
        singleMod[bestIndex]-=1
        singleModSum-=1
        prev = bestIndex
        #print(bestIndex)
        if(first==-1):
            first=bestIndex
            
    if(len(order)!=n or (order[0])==order[-1]):
        print([n,r,o,y,g,b,v])
        print(order)
    #print(order)
    return order
        
                    
numcases = int(f.readline())
for casenum in range(1,numcases+1):
    problem = f.readline().strip().split(' ')
    n = int(problem[0])
    r = int(problem[1])
    o = int(problem[2])
    y = int(problem[3])
    g = int(problem[4])
    b = int(problem[5])
    v = int(problem[6])
    #print('---')
    fo.write('Case #' + repr(casenum) + ': ' + solve(n,r,o,y,g,b,v)+'\n')
    
f.close()
fo.close()