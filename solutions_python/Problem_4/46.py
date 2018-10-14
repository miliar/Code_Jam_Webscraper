#!/usr/bin/python
import math
import sys
import string
from heapq import heappush, heappop
import random

input = "large.in"
#input = sys.argv[1]

def solve(v1, v2):
    v1.sort()
    v2.sort()
    sum = 0
    for i in range(len(v1)):
        sum += v1[i] * v2[size - i - 1]
    return sum

file = open(input)

testCases = int(file.readline())
for counter in range(testCases):
    result = ""   
    size =  int(file.readline())
    v1 = map(int, file.readline().split())
    v2 = map(int, file.readline().split())
    
    solution = solve(v1, v2)
    
    result = "Case #" + str(counter+1) + ": "
    result += str(solution)
    print result
    
