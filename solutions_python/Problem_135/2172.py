#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

IN = sys.stdin

def nextLine():
    return IN.readline().strip().split()

def nextIntLine():
    return [int(x) for x in nextLine()]

def calc():
    r1 = nextIntLine()[0]
    for r in (1, 2, 3, 4):
        t = nextIntLine()
        if r == r1:
            A = set(t)
    val = 0
    r1 = nextIntLine()[0]
    for r in (1, 2, 3, 4):
        t = nextIntLine()
        if r == r1:
            val = [x for x in t if x in A]
    if len(val) == 1:
        return val[0]
    elif len(val) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"

def main():
    T = int(IN.readline().strip())
    idx = 0
    while idx < T:
        idx += 1
        print 'Case #{0}: {1}'.format(idx, calc())

if __name__ == '__main__':
    main()
