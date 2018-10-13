# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:00:28 2017

@author: pellowes
"""

import numpy as np
import sys

fileIn = '/Users/pellowes/test.in'
fileIn = '/Users/pellowes/Downloads/A-small-attempt0(2).in'
fileOut = fileIn.split('.')[0]+'.out'

f = open(fileIn,'r')
fo = open(fileOut,'w')
    
def flip(alignment,location,length):
    newAlignment = ''    
    for i in range(0,len(alignment)):
        if(i >= location and i < location+length):
            print(i)            
            if(alignment[i]=='+'):
                newAlignment+='-'
            elif(alignment[i]=='-'):
                newAlignment+='+'
        else:
            newAlignment+=alignment[i]
    return newAlignment
    
def allPlus(alignment):
    for thing in alignment:
        if(thing == '-'):
            return False
    return True
    
def solve(original_alignment,flipper_length):
    #if the leftmost is wrong, we need to flip the leftmost
    #we never need to flip the same place twice, that's futile
    flips = 0
    alignment = original_alignment
    for i in range(0,len(original_alignment)-flipper_length+1):
        if(allPlus(alignment)):
            return str(flips)
        elif(alignment[i]=='-'):
            alignment = flip(alignment,i,flipper_length)
            print(alignment)
            flips+=1
    if(allPlus(alignment)):
            return str(flips)
    return("IMPOSSIBLE")

numcases = int(f.readline())
for casenum in range(1,numcases+1):
    problem = f.readline().strip().split(' ')
    pancakes = problem[0]
    t = int(problem[1])
    print('---')
    fo.write('Case #' + repr(casenum) + ': ' + solve(pancakes,t)+'\n')
    
f.close()
fo.close()