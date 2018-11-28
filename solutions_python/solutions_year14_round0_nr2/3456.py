#!/usr/bin/env python
#coding: utf-8
from __future__ import unicode_literals, print_function

from functools import partial
import sys
import math


def get_x(C, F, X, n):
    return X/(2+n*F) + C*sum(1/(2+j*F) for j in xrange(0, n))


def solve(C, F, X):
    lim = int(math.ceil(X/C))
    results = [get_x(C, F, X, i) for i in xrange(0, lim)]
    minimum = min(results)
    return minimum


def stdwrite(line, stdout):
    stdout.write('%s\n' % line)

def cookie(stdin, stdout):
    writeline = partial(stdwrite, stdout=stdout)
    T = int(stdin.readline())
    for i in xrange(1, T+1):
        C, F, X = map(float, stdin.readline().split(' '))
        writeline('Case #%d: %.7lf' % (i, solve(C, F, X)))

if __name__ == '__main__':
    cookie(sys.stdin, sys.stdout)
