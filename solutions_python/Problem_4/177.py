#!/usr/bin/env python
# encoding: utf-8
"""
Created by Devin Naquin on 2008-07-25.
Copyright (c) 2008. All rights reserved.
"""

import sys

def main():
    num_tests = int(sys.stdin.readline().strip())
    assert(1 <= num_tests and num_tests <= 10)
    
    for i in range(num_tests):
        # Run each test case.
        n = int(sys.stdin.readline().strip())
        assert(100 <= n and n <= 800)
        u = map(int, sys.stdin.readline().strip().split(' '))
        assert(len(u)==n)
        v = map(int, sys.stdin.readline().strip().split(' '))
        assert(len(v)==n)
        
        # Calculate
        minimum = 0
        while len(u)>0:
            m = min_pair(u,v)
            minimum += u[m[0]] * v[m[1]]
            u.pop(m[0])
            v.pop(m[1])
        
        print 'Case #%s: %s' % (i+1, minimum)

def min_pair(U, V):
    minimum, maximum = None, None
    min_i, min_j = None, None
    for i,u in enumerate(U):
        if minimum==None or u<minimum:
            minimum, min_i = u, i
    for i,v in enumerate(V):
        if maximum==None or v>maximum:
            maximum, min_j = v, i
    return (min_i, min_j)

if __name__ == '__main__':
    main()
