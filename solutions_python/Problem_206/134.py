# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 11:51:23 2017

@author: pellowes
"""


import numpy as np
import sys

fileIn = '/Users/pellowes/test.in'
fileIn = '/Users/pellowes/Downloads/A-small-attempt0(4).in'
fileIn = '/Users/pellowes/Downloads/A-large(4).in'
fileOut = fileIn.split('.')[0]+'.out'

f = open(fileIn,'r')
fo = open(fileOut,'w')
    
    
def solve(d,horses):
    longestFinishingTime = 0
    for horse in horses:
        distanceKm = d-int(horse[0])
        speedKmH = int(horse[1])
        timeH = distanceKm/speedKmH
        if timeH > longestFinishingTime:
            longestFinishingTime = timeH
    return str(d/longestFinishingTime)

numcases = int(f.readline())
for casenum in range(1,numcases+1):
    problem = f.readline().strip().split(' ')
    d = int(problem[0])
    n = int(problem[1])
    horses = []
    for row in range(0,n):
        horses.append(f.readline().strip().split(' '))
    #print('---')
    fo.write('Case #' + repr(casenum) + ': ' + solve(d,horses)+'\n')
    
f.close()
fo.close()