#!/usr/local/bin/python3.1


from functools import reduce

C = int(input())

def deltas(alist):
    return [alist[i+1] - alist[i] for i in range(len(alist)-1)]

def nextMultiple(num, multiple):
    return multiple * ((num + multiple - 1) // multiple)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for i in range(C):
    N, *Ts = (int(v) for v in input().split(' '))
    Ts.sort()
    lastEvent = Ts[0]
    multiple = reduce(gcd, deltas(Ts))
    print("Case #{}: {}".format(i + 1, nextMultiple(lastEvent, multiple) - lastEvent))
