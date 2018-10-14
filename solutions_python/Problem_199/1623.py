# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:41:16 2017

@author: willedwa
"""

def readint(): return int(input())
def readarray(x): return map(x, input().split())

def toInt(nums):
    y = []
    for x in nums:
        x = int(x)
        y.append(x)
    return y

cases = readint()
for case in range(cases):

    pancakes, size_of_flip = input().split()
    size_of_flip = int(size_of_flip)
    pancakes = list(pancakes)

    flips = 0
    for i, pancake in enumerate(pancakes):
        if pancakes.count('-') > 0:
            if pancake == '-':
                if i > len(pancakes) - size_of_flip:
                    break
                for j in range(i, i+size_of_flip):
                    if pancakes[j] == '-':
                        pancakes[j] = '+'
                    else:
                        pancakes[j] = '-'
                flips += 1
                #print 'flip',flips,pancakes
    if pancakes.count('-') > 0: flips = "IMPOSSIBLE"

    print ('Case #%i:'%(case+1), flips)