#!/usr/bin/env python2

import sys

def isp(n):
    x = str(n)
    if x == x[::-1]:
        return True
    else:
        return False

def gcj(f):
    with open(f, 'r') as datafile:
        t = int(datafile.readline())
        data = datafile.read()
        for c, dataset in enumerate(data.split("\n")):
            if dataset:
                print 'Case #{}: {}'.format(c+1, process(dataset))

def process(dataset):
    pal = [1,4,9,121,484]
    i,j = map(int, dataset.split())
    x = [y for y in pal if i <= y <= j]
    return len(x)



gcj(sys.argv[1])
