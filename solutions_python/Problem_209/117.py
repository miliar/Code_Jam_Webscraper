#!/usr/bin/env python
import numpy as np


def memf(f):
    """Takes function as an argument"""
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x] = f(*x)
        return memf.cache[x]
    memf.cache = {}
    return memf


def getMax(index, till, done):
    if(index == N):
        if(done == K):
            return till
        else:
            return -1.0
    r, h = pancakes[index]
    pancakeArea = 2*np.pi*r*h
    if(done == 0):
        pancakeArea += np.pi*r*r
    sel1 = getMax(index+1, till+pancakeArea, done+1)
    sel2 = getMax(index+1, till, done)
    if(sel1 == -1):
        return sel2
    if(sel2 == -1):
        return sel1
    return max(sel1, sel2)


inFile = open('in.txt', 'r')
outFile = open('out.txt', 'w')
getMax = memf(getMax)
pancakes = []
N = 0
K = 0
t = int(inFile.readline())
for test in range(1, t+1):
    getMax.cache = {}
    N, K = map(int, inFile.readline().split(' '))
    pancakes = []
    for pancake in range(N):
        r, h = map(int, inFile.readline().split(' '))
        pancakes.append((r, h))
    pancakes.sort(key=lambda pancake: pancake[0])
    pancakes.reverse()
    # print pancakes
    ans = getMax(0, 0.0, 0)
    outFile.write("Case #{}: {}\n".format(test, ans))
