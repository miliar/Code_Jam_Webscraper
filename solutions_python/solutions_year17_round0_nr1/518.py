#!/usr/bin/env python2
# -*- coding: utf-8 -*-

           
t = int(raw_input())

for test_case in range(1, t+1):
    #read test case
    pnks, K = raw_input().split(" ")
    K = int(K)
    pnks = list(pnks)
    
    #Solve the problem
    n = len(pnks)
    flips = 0
    for i in range(n-K+1):
        if pnks[i] == '-':
            # flip next K pancakes
            flips += 1
            for j in range(K):
                pnks[i+j] = '+' if pnks[i+j] == '-' else '-'
    
    solution = str(flips)
    for i in range(n-K, n):
        if pnks[i] == '-':
            solution = 'IMPOSSIBLE'
            break

    print "Case #{}: {}".format(test_case, solution)