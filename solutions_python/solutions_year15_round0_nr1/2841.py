#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: penguin
# @Date:   2014-01-18 16:48:42
# @Last Modified by:   penguin
# @Last Modified time: 2014-01-18 19:53:56

def solve(c, i):
    # max_shy = i[0]
    num_p_stand = 0
    num_p_needed = 0
    for j, k in enumerate(str(i[1])):
        if j == 0:
            num_p_stand += int(k)
        else:
            if num_p_stand >= j:
                num_p_stand += int(k)
            else:
                if int(k) >0:
                    num_p_needed += (j - num_p_stand)
                    num_p_stand += (j - num_p_stand)+int(k)
    dst.write("Case #{0}: {1}\n".format(c, num_p_needed))


src = open('A-large.in')
dst = open('A-small-attempt0.out', 'w')

testCases = int(src.readline().rstrip())
for y in xrange(0, testCases):
    solve(y+1, src.readline().split("\n")[0].split(" "))
    
src.close()
dst.close()