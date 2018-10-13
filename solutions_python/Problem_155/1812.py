#!/bin/env python

'''
Created on 11.04.2015

@author: Dennis Nienhüser <earthwings@gentoo.org>
'''

import sys

inputFile = open(sys.argv[1], 'r')
problems = int(inputFile.readline())
for problemIndex in range(problems):
    totalMissing = 0
    standing = 0
    problem = inputFile.readline().strip().split(' ')
    shyness = problem[1]
    for index in range(int(problem[0])+1):
        missing = max(0, index-standing)
        totalMissing += missing
        standing += int(shyness[index]) + missing
    
    print ('Case #' + str(problemIndex+1) + ': ' + str(totalMissing))
