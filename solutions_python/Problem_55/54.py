#!/usr/bin/python

import sys
from math import *

C = int(sys.stdin.readline())

for testcase in range(C):
    line = sys.stdin.readline().strip().split()
    R = long(line[0])
    k = long(line[1])
    N = long(line[2])
    line = sys.stdin.readline().strip().split()

    g = []
    for j in range(N):
        g.append(long(line[j]))

    r_index = [-1] * N;
    r_index[0] = 1
    money_index = [-1] * N;
    money_index[0] = 0

    endflag = False
    
    index = 0
    r = 1
    money = 0

    cycler = 0
    cycle = 0
    cycle_money = 0
    r_to_cycle = 0
    money_to_cycle = 0
    
    while True:
        #print r_index
        #print money_index
        summation = 0
        next = index
        for i in range(index,N) + range(0,index):
            if summation + g[i] > k:
                break
            summation += g[i]
            next = i
            
        money += summation
        index = (next + 1) % N
        r += 1
        if r > R:
            print "Case #%d: %d" % (testcase+1,money)
            endflag = True
            break

        if r_index[index] == -1:
            r_index[index] = r
            money_index[index] = money
        else:
            cycler = index
            cycle = r - r_index[index]
            cycle_money = money - money_index[index]
            money_to_cycle = money_index[index]
            r_to_cycle = r_index[index]-1

            #print "cycler=",cycler,"cycle=",cycle,"cycle_money=",cycle_money,"money_to=",money_to_cycle,"r_to=",r_to_cycle
            break
        
    if endflag:
        continue

    result_money = 0
    R -= r_to_cycle
    result_money += money_to_cycle

    result_money += R / cycle * cycle_money
    R = R % cycle


    index = cycler

    for i in range(R):
        summation = 0
        next = index
        for i in range(index,N) + range(0,index):
            if summation + g[i] > k:
                break
            summation += g[i]
            next = i
            
        result_money += summation
        index = (next + 1) % N

    print "Case #%d: %d" % (testcase+1,result_money)
    
    
        
