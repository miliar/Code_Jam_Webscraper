#!/usr/bin/env python

import sys

def solve(num, seq):
    # p: current point of O and B 
    p = [1, 1]
    # s: stored allowed move time of O and B
    s = [0, 0]
    sum = 0
    for item in seq:
        if item[0] == 'O':
            target = 0
            stay = 1
        else:
            target = 1
            stay = 0
            
        left = abs(item[1] - p[target])
        left -= s[target]
        if left < 0:
            left = 0

        time = left + 1
        s[stay] += time
        sum += time

        p[target] = item[1]
        s[target] = 0

    print 'Case #' + str(num) + ': ' + str(sum)

from automain import *
@automain
def main():
    fi = sys.stdin
    lines = fi.readlines()
    T = int(lines[0])
    for i in xrange(1, T+1):
        fields = lines[i].strip('\n').split(' ')
        N = int(fields[0])
        test = [[fields[j], int(fields[j+1])] for j in xrange(1, 2*N, 2)]
        solve(i, test)

