#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin
import sys
sys.setrecursionlimit(100005)

# assumption: integer lookups are faster
quarts = {'1': 1, 'i': 2, 'j': 3, 'k': 4, 
          '-1': -1, '-i': -2, '-j': -3, '-k': -4, 
          1: '1', 2: 'i', 3: 'j', 4: 'k', 
          -1: '-1', -2: '-i', -3: '-j', -4: '-k'}

table = {
    (1, 1): 1,
    (1, 2): 2,
    (1, 3): 3,
    (1, 4): 4,
    
    (2, 1): 2,
    (2, 2): -1,
    (2, 3): 4,
    (2, 4): -3,
    
    (3, 1): 3,
    (3, 2): -4,
    (3, 3): -1,
    (3, 4): 2,
    
    (4, 1): 4,
    (4, 2): 3,
    (4, 3): -2,
    (4, 4): -1,
}

def multiply(a, b):
    negs = 0
    negs += 1 if a < 0 else 0
    negs += 1 if b < 0 else 0
    
    cc = table[abs(a), abs(b)]    
    cc *= -1 if negs == 1 else 1
    return cc

fail = set()

def find(curr, s, pos, trgt):
    #print "find %s, %s, %d, %s" % (curr, s, pos, trgt)
    if len(trgt) == 0:
        return 'YES' if pos == len(s) else 'NO'

    if pos >= len(s):
        return 'NO'
    if (curr, pos, trgt[0]) in fail:
        return 'NO'

    next = multiply(curr, s[pos])
    
    # A] continue searching
    res = find(next, s, pos+1, trgt)
    if res == 'YES':
        return 'YES'
   
    # B] try to advance to next target
    if next == trgt[0]:
        res =  find(1, s, pos+1, trgt[1:])
        if res == 'YES':
            return 'YES'
        
    fail.add((curr, pos, trgt[0]))
    return 'NO'

def solveCase():    
    L, X = map(int, stdin.readline().split())
    s = stdin.readline().strip()
    ss = map(lambda x : quarts[x], X * s)
    
    fail.clear()
    print find(1, ss, 0, map(lambda x : quarts[x], "ijk"))

# main
caseCnt = int(stdin.readline())

for caseNr in range(1, caseCnt + 1):
    print "Case #" + str(caseNr) + ":",
    solveCase()
