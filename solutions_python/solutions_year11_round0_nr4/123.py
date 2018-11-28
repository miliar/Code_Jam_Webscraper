#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

def solve(numbers):
    return len([i for i, v in enumerate(numbers, 1) \
                  if i != v \
                ])

def main():
    T = int(sys.stdin.readline())
    for i in xrange(T):
        sys.stdin.readline()
        numbers = map(int, sys.stdin.readline().split())
        ret = solve(numbers)
        print "Case #" + str(i+1) + ": " + str(ret)

if __name__ == '__main__':
    main()
