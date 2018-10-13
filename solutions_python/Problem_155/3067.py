#!/usr/bin/env python

from __future__ import print_function

try:
    input = raw_input
except NameError:
    pass

def test(pop) :
    tot = 0
    add = 0

    for i, num in enumerate(pop) :
        if tot>=i:
            tot+=int(pop[i])
        else:
            add+=i-tot
            tot+=i-tot+int(pop[i])

    return add

T = int(input())

tests = [input().split() for _ in range(T)]

case = 1
for case in range(T) :
    print("Case #{}: {}".format(case+1, test(tests[case][1])))