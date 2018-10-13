#!/usr/bin/python
import math
import sys
import string
from heapq import heappush, heappop
import random
import os

#mainInput = "large.in"
#input = "input"
input = sys.argv[1]

def solve(m,v, input, node):
    b = ((m-1)/2)
    tree = [m+1] * m
    res = [m+1] * m
    #print len(input), m
    for i in range ((m+1)/2):
        k = m - 1 - i
        tree[k] = input[k]
    for i in range ((m-1)/2):
        k = (m-1)/2 - i - 1
        #print "k: " + str( k)
        if input[k][0] == 0: #OR gate
            tree[k] = tree[2*k+1] or tree[2*k+2]
            if input[k][1] == 0: #NOT CHANGABLE
                if tree[2*k+1] and  tree[2*k+2]:
                    res[k] = res[2*k+1] + res[2*k+2]
                elif tree[2*k+2] and (not tree[2*k+1]):
                    res[k] = res[2*k+2]
                elif (not tree[2*k+2]) and  tree[2*k+1]:
                    res[k] = res[2*k+1]
                else:
                    res[k] = min(res[2*k+2] , res[2*k+1])
            if input[k][1] == 1: #CHANGABLE
                if tree[2*k+2] and  tree[2*k+1]:
                    res[k] = min(res[2*k+2], res[2*k+1]) + 1
                elif tree[2*k+2] and (not tree[2*k+1]):
                    res[k] = 1
                elif (not tree[2*k+2]) and  tree[2*k+1]:
                    res[k] = 1
                else:
                    res[k] = min(res[2*k+2] , res[2*k+1])
        if input[k][0] == 1: #AND gate
            tree[k] = tree[2*k+2] and tree[2*k+1]
            if input[k][1] == 0: #NOT CHANGABLE
                if tree[2*k+2] and  tree[2*k+1]:
                    res[k] = min(res[2*k+2] , res[2*k+1])
                elif tree[2*k+2] and (not tree[2*k+1]):
                    res[k] = res[2*k+1]
                elif (not tree[2*k+2]) and  tree[2*k+1]:
                    res[k] = res[2*k+2]
                else:
                    res[k] = res[2*k+2] + res[2*k+1]
            if input[k][1] == 1: #CHANGABLE
                if tree[2*k+2] and  tree[2*k+1]:
                    res[k] = min(res[2*k+2], res[2*k+1])
                    #print "here:  " 
                    #print res[k]
                elif tree[2*k+2] and (not tree[2*k+1]):
                    res[k] = 1
                    #print "here: 2 " 
                elif (not tree[2*k+2]) and  tree[2*k+1]:
                    res[k] = 1
                    #print "here: 3 " 
                else:
                    res[k] = min(res[2*k+2] , res[2*k+1]) + 1
                    #print "here: 4 " 
                    #print res[k]
        #print tree
        #print res
    if (tree[0] - v) == 0: return 0
    else: 
        return res[0]

file = open(input)
testCases = int(file.readline())
for counter in range(testCases):
    result = ""   

    line = map(int, file.readline().split())
    (m,v) = line
    input = []
    for i in range((m-1)/2):
        line = map(int, file.readline().split())
        input.append(line)
    for i in range((m+1)/2):
        line = map(int, file.readline().split())
        input.append(line[0])
    #print m, v, tree
    #if v == tree[0][0]: solution = 0
    solution = solve(m, v, input, 0)
    if solution >= m:
        solution = "IMPOSSIBLE"
    result = "Case #" + str(counter + 1) + ": "
    result += str(solution)
    print result
    
