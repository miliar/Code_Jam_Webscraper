#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import itertools
#import pygraph
#from pygraph.classes.graph import graph

def solve(r,k,n,groups):
    pos = 0
    cost = 0
    for i in xrange(r):
        place = 0
        count = 0
        while (place + groups[pos]) <= k and count < n:
            place += groups[pos]
            pos = (pos + 1) % n
            count += 1
        #print place
        cost += place
    result = cost
    return result

def main():
    #max recursion limit
    sys.setrecursionlimit(sys.maxint)
    input = open('inputs.txt', 'rU')
    output = open('outputs.txt', 'w')
    N = int(input.readline())
    i = 1;
    while i <= N:
        line = input.readline()
        values = line.split()
        r = long(values[0])
        k = long(values[1])
        n = long(values[2])
        line = input.readline()
        values = line.split()
        groups = []
        for j in xrange(n):
            groups.append(long(values[j]))
        result = solve(r,k,n,groups)
        print 'Case #%d: ' % (i) + str(result)
        output.write('Case #%d: ' % (i) + str(result) + '\n')
        i += 1
    input.close()
    output.flush()
    output.close()
    return 0

if __name__ == '__main__':
    main()
