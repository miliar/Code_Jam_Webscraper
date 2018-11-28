import sys
import math
import heapq
import random

def count(c):
    if c == 1:
        return 1
    if c == 2:
        return 2
    
    return count(c/2) + 1

def task(L, P, C):
    if L * C >= P:
        return 0
    
    c = 0
    tmp = L
    while tmp*C < P:
        tmp *= C
        c += 1
    
    print c
    return count(c)
    

if __name__ == '__main__':
    #in_file = 'testB.txt'
    #in_file = 'B-small-attempt0.in'
    in_file = 'B-large.in'
    out_file = 'res'
    
    lines = open(in_file).readlines()    
    lines = lines[1:]
    
    wfile = open(out_file, 'w')
    
    case = 0
    while lines:
        case += 1
        wfile.write('Case #' + str(case) + ': ')
        
        # coding begins here
        L, P, C = lines[0].strip().split()
        lines = lines[1:]
        L = int(L); P = int(P); C = int(C)
        
        res = task(L, P, C)
        wfile.write(str(res) + '\n')
        
        
    wfile.close()



# END