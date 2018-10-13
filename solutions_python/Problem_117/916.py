#!/usr/bin/env python
# coding=utf-8

import sys
import numpy as np

def solve(N, M, lawn):
    a = np.array(lawn)
    #print a

    while a.size:
        argmin = np.argmin(a)
        x, y = argmin/M, argmin%M
        minval = a[x, y]
        #print (x, y), minval

        line = a[x,:]
        col = a[:,y]
        #print line, col

        if max(line) == minval:
            a = np.delete(a, x, 0)
            N -= 1
        elif max(col) == minval:
            a = np.delete(a, y, 1)
            M -= 1
        else:
            return 'NO'
        #print a

    return 'YES'

def main():
    with open(sys.argv[1]) as f:
        T = int(f.readline().strip())
        for i in xrange(T):
            lawn = []
            N, M = (int(x) for x in f.readline().strip().split())
            for j in xrange(N):
                lawn.append([int(x) for x in f.readline().strip().split()])
            res = solve(N, M, lawn)
            print 'Case #%d: %s' % (i+1, res)

if __name__ == "__main__":
    main()
