#!/usr/bin/env python3
#-*- coding:utf-8 -*-

n = int(input())

for i in range(n):
    (x, line) = input().split()
    total = 0
    res = 0
    for (level, num) in enumerate(line):
        level = int(level)
        num = int(num)
        if level > total and level > 0 and num > 0:
            res += level - total
            total += level - total
        total += num
    print ("Case #%d: %d" % (i + 1, res))

