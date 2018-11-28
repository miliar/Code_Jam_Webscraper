#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# Input
  	
# Output
 
# 2
# 2 20 8 2 3 5
# 1 4 2 2 10 4
# 	Case #1: 54
# Case #2: 20


f = open(sys.argv[1])
nb_case = int(f.readline())
for i in range(nb_case):
    response = 0
    li = f.readline()[:-1].split(" ")
    L = int(li[0])
    t = int(li[1])
    N = int(li[2])
    c = int(li[3])
    dist = []
    stars = []
    for d in li[4:]:
        dist.append(int(d))
    for j in range(N):
        stars.append(dist[j%c])
    
    time_to_build = t
    stars_with_boost = []
    for j, s in enumerate(stars):
        if (time_to_build - 2*s) < 0:
            stars_with_boost.append((2*s - time_to_build)/2)
            stars_with_boost.extend(stars[j+1:])
            response += time_to_build
            break
        response += 2*s
        time_to_build -= 2*s
    stars_with_boost = sorted(stars_with_boost, reverse=True)
    for s in stars_with_boost:
        if L != 0:
            L -= 1
            response += s
            continue
        response += 2*s
    print("Case #" + str(i+1) + ": " + str(response))
    
