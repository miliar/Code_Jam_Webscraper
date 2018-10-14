#!/usr/bin/env python

from math import *

def solve():
    'Solution goes here'
    pass

if __name__ == '__main__':
    from sys import stdin
    def read_line():    return stdin.readline()
    def read_words():   return read_line().split()
    def read_ints():    return map(int, read_words())
    def read_floats():  return map(float, read_words())

    cases, = read_ints()
    for c in range(cases):
        # Read parameters
        ans = solve()
        print 'Case #%d:'%(c+1), ans
