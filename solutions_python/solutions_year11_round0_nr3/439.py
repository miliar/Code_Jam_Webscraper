#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) !=2:
    sys.exit()

f = open(sys.argv[1],"r")

T = 0
i = 0
case = 0
for line in f:
    i = i + 1
    if i == 1:
        T = int(line)
    else:
        if i % 2 == 0:
            N = int(line)
        else:
            cand = line.strip().split(" ")
            case = case + 1
            #print cand
            result = 0
            candies = []
            for c in cand:
                candies += [int(c),]
                result ^= int(c)
            if result != 0:
                out = "NO"
            else:
                candies = sorted(candies)
                candies = candies[1:]
                #print candies
                result = 0
                for c in candies:
                    result += c
                out = result

            print "Case #%d:" % (case),out

f.close()
