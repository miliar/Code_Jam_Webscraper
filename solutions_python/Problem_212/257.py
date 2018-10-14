#!/usr/bin/env python

def parseline():
    s = input().split(' ')
    return [int(i) for i in s]

t = int(input())
for case in range(1, t+1):
    n, p = parseline()
    groups = [i%p for i in parseline()]
    fresh = groups.count(0)
    if p == 2:
        fresh += (groups.count(1) + 1)//2
    elif p == 3:
        twos = groups.count(2)
        ones = groups.count(1)
        fresh += min(twos, ones) + (abs(twos - ones) + 2)//3
    elif p == 4:
        raise Exception(p)
    else:
        raise Exception(p)

    print(f'Case #{case}: {fresh}')
