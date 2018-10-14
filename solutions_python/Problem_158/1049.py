#!/bin/env python

'''
Created on 11.04.2015

@author: Dennis Nienhüser <earthwings@gentoo.org>
'''

import sys, math

def vectorize(line):
    'converts a whitespace separated string of numbers into a list with integers'
    items = line.strip().split(sep=' ')
    for index, item in enumerate(items):
        items[index] = int(item)
    return items

def canSolve(xomino, cols, rows):
    'return True iff a xomino board with a size of cols x rows can be solved while containing an arbitrary xomino shape'
    assert (xomino >= 1 and xomino <= 4)
    assert (cols >= 1 and cols <= 4)
    assert (rows >= 1 and rows <= 4)
    
    if xomino == 1:
        # we can fit any block
        return True
   
    if xomino > rows and xomino > cols:
        # the board is too small
        return False
    
    if (cols * rows) % xomino != 0:
        # the number of blocks does not fit into the board exactly
        return False 

    smallerSide = min( rows, cols )
    if math.ceil( xomino / 2.0 ) > smallerSide:
        # rectangle-like shapes must fit
        return False

    if xomino == 4:
        # 2,2 is too small; 2,3 is ruled out above already 
        return rows > 2 and cols > 2
    
    return True

with open(sys.argv[1], 'r') as inputFile: 
    problems = int(inputFile.readline())
    for problem in range(problems):
        plates = vectorize(inputFile.readline())
        winner = 'GABRIEL' if canSolve(plates[0], plates[1], plates[2]) else 'RICHARD'
        print ('Case #' + str(problem + 1) + ': ' + str(winner))
