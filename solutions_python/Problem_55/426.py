#!/usr/bin/python

import os
import sys
import math
import fractions

infile = open(sys.argv[1])

line_num = int(infile.readline())

for i in range(line_num):
    line = infile.readline()
    items = line.split(' ')
    R = int(items[0])
    k = int(items[1])
    N = int(items[2])
    line = infile.readline()
    items = line.split(' ')
    nums = [int(x) for x in items]
    order = nums[:]
    profit = 0
    roun = 1
    while roun <= R:
        cap = k
        gcount = 0
        while True:
            top = order[0]
            if cap >= top:
                profit += top
                cap -= top
                order.remove(top)
                order.append(top)
                gcount += 1
                if gcount >= len(nums):
                    break
            else:
                break
        if order == nums:
            profit *= R / roun
            roun = (R / roun) * roun
        roun += 1
    
    print 'Case #' + str(i + 1) + ':', str(profit)


    
