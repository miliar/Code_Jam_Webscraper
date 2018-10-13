#!/usr/bin/env python
import sys

num_cases = -1

fileIN = open(sys.argv[1], "r")

num_cases = int(fileIN.readline())

for case_num in range(num_cases):
    num_items = int(fileIN.readline())
    vector1 = [int(x) for x in fileIN.readline().split()]
    vector2 = [int(x) for x in fileIN.readline().split()]
    
    vector1.sort()
    vector2.sort()
    vector2.reverse()
    
    products = []
    for i in range(num_items):
        products.append(vector1[i] * vector2[i])

    sys.stdout.write("Case #" + str(case_num+1) + ": " + str(sum(products)) + "\n")
