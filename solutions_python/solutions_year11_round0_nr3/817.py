#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

f = open(sys.argv[1])
nb_case = int(f.readline())
for i in range(nb_case):
    nb_number = int(f.readline())
    req = f.readline().split(" ")
    r = []
    sum = 0
    mini = 100000000
    for j in req:
        r.append(int(j))
        sum ^= int(j)
        if int(j) < mini:
            mini = int(j)
    if sum != 0:
        print("Case #" + str(i+1) + ": NO")
        continue
    r.remove(mini)
    response = 0
    for j in r:
        response += j
    print("Case #" + str(i+1) + ": " + str(response))
    
