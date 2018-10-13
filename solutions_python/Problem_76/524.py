#!/usr/bin/env python
from itertools import *
import sys, operator

def badadd(x,y):
    small,big = map(lambda s: bin(s)[2:], sorted([x,y]))
    diff = len(big) - len(small)
    result = big[:diff]
    for i,c1 in enumerate(small):
        c2 = big[i+diff]
        if c1==c2:
            result += '0'
        else:
            result += '1'
    return int(result,2)

def all_sublists(lst):
    result = []
    for i in range(1,len(lst)):
        result.extend(combinations(lst,i))
    return result

def solve(candy):
    total = reduce(operator.add, candy)
    splits = []
    for sl in all_sublists(candy):
        val = reduce(badadd,sl)
        diff = [item for item in candy]
        [diff.remove(item) for item in sl]
        if val == reduce(badadd, diff):
            splits.append(total-reduce(operator.add,sl))
    if len(splits) == 0:
        return "NO"
    if max(splits) == 0:
        return "NO"
    return str(max(splits))
    
with open(sys.argv[1]) as file:
    for i,line in enumerate(islice(file, 2, None, 2)):
        candy = map(int, line.split(" "))
        result = solve(candy)
        print "".join(["Case #",str(i+1),": ", result])
