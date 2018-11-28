#!/usr/bin/python

import sys
import re
import math
import fractions

def find_best(boxes, toys):
    if len(boxes) == 0 or len(toys) == 0:
        return 0
    if find_best.cache.has_key((len(boxes), len(toys), boxes[0][0], toys[0][0])):
        return find_best.cache[(len(boxes), len(toys), boxes[0][0], toys[0][0])] 
    if boxes[0][1] == toys[0][1]:
        if boxes[0][0] == toys[0][0]:
            r = boxes[0][0] + find_best(boxes[1:], toys[1:])
        elif boxes[0][0] < toys[0][0]:
            tn = toys[:]
            tn[0] = (tn[0][0] - boxes[0][0], tn[0][1])
            r = boxes[0][0] + find_best(boxes[1:], tn)
        else:
            bn = boxes[:]
            bn[0] = (bn[0][0] - toys[0][0], bn[0][1])
            r = toys[0][0] + find_best(bn, toys[1:])
    else:
        r = max(find_best(boxes[1:], toys), find_best(boxes, toys[1:]))
    find_best.cache[(len(boxes), len(toys), boxes[0][0], toys[0][0])] = r
    return r

f = open(sys.argv[1],'r')
num = int(f.readline())
for z in range(num):
    n,m = [int(x) for x in f.readline().split()]
    boxes = [int(x) for x in f.readline().split()]
    toys = [int(x) for x in f.readline().split()]
    boxes = [(boxes[i], boxes[i+1]) for i in range(0,2*n,2)]
    toys = [(toys[i], toys[i+1]) for i in range(0,2*m,2)]
    #print n, m, boxes, toys
    find_best.cache = {}
    best = find_best(boxes, toys)
    print 'Case #{}:'.format(z+1), best
    sys.stdout.flush()
