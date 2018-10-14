#!/usr/bin/env python
from __future__ import print_function
import sys
import time
from functools import reduce

if '-d' in sys.argv[1:]:
    def dbg(s):
        sys.stderr.write(s)
        sys.stderr.flush()
else:
    def dbg(x):
        pass

def readline():
    return sys.stdin.readline().strip()

def readfloat():
    return float(readline())

def readfloats():
    return [float(x) for x in readline().split()]

def readint():
    return int(readline())

def readints():
    return [int(x) for x in readline().split()]

def car(x):
    try:
        return x[0]
    except IndexError:
        return None

def cdr(x):
    return x[1:]

def solve_case():
    _, s = readline().split()
    D = [int(c) for c in s]
    invited = 0
    standing = 0
    for shyness, n in enumerate(D):
        i = 0
        if shyness > standing:
            i = shyness - standing
            invited += i
        standing += n + i
    return invited

def main():
    cases = readint()
    for c in range(1, cases + 1):
        t0 = time.time()
        sys.stdout.write('Case #{0:d}: {1}\n'.format(c, solve_case()))
        sys.stdout.flush()
        dbg('t {:.6f}\n'.format(time.time() - t0))

if __name__ == '__main__':
    main()

