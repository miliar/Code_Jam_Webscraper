#!/usr/bin/env python3

import sys

def getline():
    return sys.stdin.readline()

def getint():
    return int(getline())

def getints():
    return [int(v) for v in getline().split()]

import collections
import math

cases = getint()
for case in range(1, cases + 1):

    diners = getint()
    hist = sorted(collections.Counter(getints()).items(), reverse=True)

    res = maxsize = hist[0][0]

    try:
        for target in range(maxsize - 1, 0, -1):
            splitcost = 0
            for size, cnt in hist:
                if size <= target:
                    break
                splitcost += cnt * math.ceil(size / target - 1)
            if splitcost > res:
                raise Exception
            newres = splitcost + target
            if newres < res:
                res = newres
    except Exception:
        pass
    
    # data = collections.Counter(getints())
    # maxsize = max(data)
    # data = [data[i] for i in range(0, maxsize + 1)]
    # splitcost = 0
    # print(maxsize, splitcost, data)
    # res = maxsize + splitcost
    
    # while maxsize > 2:
    #     splitcost += data[maxsize]
    #     if splitcost >= res:
    #         break
    #     cnt = data[maxsize]
    #     data[maxsize] = 0
    #     half = maxsize // 2
    #     data[half] += cnt
    #     data[half + maxsize % 2] += cnt
    #     while data[maxsize] == 0:
    #         maxsize -= 1
    #     print(maxsize, splitcost, data)
    #     newres = splitcost + maxsize
    #     if newres < res:
    #         res = newres 
            
    print('Case #{}: {}'.format(case, res))
    
