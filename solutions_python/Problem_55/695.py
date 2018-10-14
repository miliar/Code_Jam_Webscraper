#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Google Code Jam 2010: Round 1 - Task C

import psyco
psyco.full()

file = open("C-small-attempt0.in", 'r')
start = True
count = 1
for line in file.readlines()[1:]:
    if start:
        start = False
        R, k, N = map(int, line.split(" "))
    else:
        start = True
        groups = map(int, line.split(" "))
        money = 0
        for r in range(0, R): # The roller coaster will run R times in a day.
            peopleIn = 0
            for g in groups:
                peopleIn += groups[0]
                if(peopleIn > k): # The roller coaster can hold k people at once. 
                    break
                tmp = groups[0]
                money += tmp
                del groups[:1]
                groups.append(tmp)
        print "Case #" + str(count) + ": " + str(money)
        count += 1
