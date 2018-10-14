#!/usr/bin/python

import sys

def gcd(a, b):
    x = a
    y = b
    if x < y:
        x = b
        y = a
    while y > 0:
        tmp = x % y
        x = y
        y = tmp
    return x

n = int(sys.stdin.readline())
cnt = 1
while cnt <= n:
    line = sys.stdin.readline()
    arr = map(int, line.split(' '))
    del arr[0]
    arr.sort()
    t = 0
    for elem in arr:
        t = gcd(elem-arr[0], t)

    i = 1
    while i <= t:
        if t % i != 0:
            i += 1
            continue
#If a+y % T == 0, b+y, c+y, ... is multiple of T
#minimum y = T-a
        tt = t / i
        y = tt-arr[0]
        if y < 0:
            y += tt * (abs(y)/tt)
            if y < 0:
                y += tt
        if all(map(lambda x: (x+y)%tt == 0, arr)):
            print 'Case #%d: %d' % (cnt, y)
            break
        i += 1

    cnt += 1
