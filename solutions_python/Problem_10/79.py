#!/usr/bin/env python

from sys import *
from math import *

def processCase(P, K, L, letters, case):
    letters.sort()
    letters.reverse()
    
    if P*K < L:
        print "Case #%d: Impossible" % (case)
        return    
    
    free = []
    for i in range(0, K):
        free.append(P)
        
    count = 0
    idx = 0    
    while len(letters) > 0:
        if idx >= K:
            idx = 0
            continue
        
        if free[idx] == 0:
            idx += 1
            
        f = free[idx] 
        free[idx] = free[idx] - 1
        idx += 1
        
        c = letters.pop(0)
        count = count + c * (P - f + 1)
    
    print "Case #%d: %d" % (case, count)
        
    return

def process(lines):
    N = int (lines[0])
    case = 1
    i = 1
    while case <= N:
        (P, K, L) = lines[i].strip("\r\n").split(' ')
        i += 1
        
        arr = lines[i].strip("\r\n").split(' ')
        i += 1
        
        letters = []
        for j in range(0, int (L)):
            letters.append(int (arr[j]))
            
        processCase(int (P), int (K), int(L), letters, case)
        case += 1
        

def usage():
    print "Usage %s input" % argv[0]

def main():    
    if len(argv) < 2:
        usage()
        exit()
        
    input = argv[1]
    f = open(input, 'r')
    
    try:
        lines = f.readlines()
        process(lines)
        
    finally:
        f.close()

if __name__ == '__main__':
    main()