import time
from sys import *
import copy 
import math    
import os
import collections
import itertools
import heapq
import sets
import random
import unittest

cases = int(raw_input())


def checkchar(char,lines):
    checks=0
    for i in xrange(4):
        for j in xrange(4):
#            print i,j,lines[i][j]        
            if lines[i][j]==char or lines[i][j]=='T':
                checks+=1
        if checks==4:
#            print 'TRUE'
            return True
        checks=0
    for j in xrange(4):
        for i in xrange(4):
            if lines[i][j]==char or lines[i][j]=='T':
                checks+=1
        if checks==4:
            return True
        checks=0        
    for i in xrange(4):
        if lines[i][i]==char or lines[i][i]=='T':
                checks+=1
    if checks==4:
        return True
    checks=0
    for i in xrange(4):
        if lines[3-i][i]==char or lines[3-i][i]=='T':
                checks+=1
    if checks==4:
        return True
    checks=0               
    return False        
             

def solve():
    lines=[]
    for _ in xrange(4):
        lines.append(raw_input().strip())
    raw_input()        
    x=checkchar('X',lines)
    y=checkchar('O',lines)
    
    if (x and y):
        return 'Draw'                
    elif x:
        return 'X won'
    elif y:
        return 'O won'
    elif all('.' not in line for line in lines):
        return 'Draw'                  
    else:
        return 'Game has not completed'
    
for case in xrange(1, cases + 1):    
    print "Case #%s: %s" % (case, solve())