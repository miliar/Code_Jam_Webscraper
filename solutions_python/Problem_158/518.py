#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin

def solve():
    X, R, C = map(int, stdin.readline().split())
    #print "%dx%d, %d:" % (R,C, X),
    
    # hole stones
    #            
    #   [][][]   
    #   []  []   
    #   [][]     
    #            
    if X >= 7:
        return 'RICHARD'

    # zick-zack stone special case
    # 
    #   [][]     
    #     [][]     
    #  
    if X == 4 and (R == 2 or C == 2):
        return 'RICHARD'

    # not modulus 0
    if R * C % X <> 0:
        return 'RICHARD'

    # long stones
    #            
    #   []       
    #   []       
    #   []      
    #   []      
    #   []      
    #   []       
    #           
    if X > R and X > C:
        return 'RICHARD'

    # space filling stones
    #            
    #   []       
    #   []       
    #   []       
    #   [][][][] 
    #            
    maxDiameter = (X + 1) / 2
    if maxDiameter > R or maxDiameter > C:
        return 'RICHARD'    

    return 'GABRIEL'

caseCnt = int(stdin.readline())

for caseNr in range(caseCnt):
	print "Case #" + str(caseNr + 1) + ":", solve()
