#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Kai Zhang(hapsunday@gmail.com)

import sys

IN = sys.stdin

def nextLine(c=None):
    if c is None:
        return IN.readline().strip().split()
    return [c(x) for x in IN.readline().strip().split()]

def calc(C, F, X):
    if X <= C:
        return X * 0.5
    idx = 0
    prev = 0
    sp = 2.0
    ret = X * 0.5
    while prev < ret:
        idx += 1
        cur = prev + C / sp
        prev = cur
        sp += F
        ans = cur + (X / sp)
        if ans < ret:
            ret = ans
    return ret

def main():
    T = nextLine(int)[0]
    idx = 0
    while idx < T:
        idx += 1
        C, F, X = nextLine(float)
        print 'Case #%d: %.8f' % (idx, calc(C, F, X))

if __name__ == '__main__':
    main()
                    
