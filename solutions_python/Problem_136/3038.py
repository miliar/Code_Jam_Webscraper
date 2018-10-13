#!/usr/bin/python

from sys import stdin

def solve():
    c, f, x = map(float, stdin.readline().split())
    curTime = 0
    farms = 0
    paybackTime = c / f
    time = 0
    while True:
        predictedTime = x / (2 + farms * f)
        buyTime = c / (2 + farms * f)
        if predictedTime > buyTime + paybackTime:
            time += buyTime
            farms += 1
        else:
            return time + predictedTime


t = int(stdin.readline())
for i in range(t):
    print('Case #%d:' % (i + 1), solve())


