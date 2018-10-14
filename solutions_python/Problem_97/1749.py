#!/usr/bin/env python
#-*- coding: utf-8 -*- 
import sys
from collections import deque

def is_recycled(n, m, a, b):
    if m <= n or n < a or m > b: #out of bounds
        return False    
    else:               
        n_dq = deque(str(n))
        m_dq = deque(str(m))
        for i in m_dq:
            if n_dq == m_dq:
                return True
            n_dq.rotate(1)
        return False

def process_case(case):
    low_num, up_num = (int(x) for x in case.split())
    recycled = 0
    for n in range(low_num,up_num+1): #brute force approach
        for m in range(n, up_num+1):
            if is_recycled(n, m, low_num, up_num):
                recycled += 1
    return recycled

if __name__ == '__main__':
    f = open (sys.argv[1], 'r')
    test_cases = int(f.readline())
    for i in range(test_cases):
        case = f.readline()
        #print case,
        recycled = process_case(case)
        print "Case #%i: %s" %(i + 1, recycled)