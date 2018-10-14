#!/usr/bin/env python
#coding: utf-8
from __future__ import unicode_literals, print_function
import sys
from functools import partial

def stdwrite(line, stdout):
    stdout.write('%s\n' % line)

def magic(stdin, stdout):
    writeline = partial(stdwrite, stdout=stdout)
    T = int(stdin.readline())
    for i in xrange(1, T+1):
        rownum1 = int(stdin.readline())
        for j in xrange(1, 4+1):
            line = stdin.readline()
            if j == rownum1:
                row1 = map(int, line.split(' '))
        rownum2 = int(stdin.readline())
        for j in xrange(1, 4+1):
            line = stdin.readline()
            if j == rownum2:
                row2 = map(int, line.split(' '))
        intersection = set(row1).intersection(set(row2))
        if len(intersection) == 0:
            writeline('Case #%d: Volunteer cheated!' % i)
        elif len(intersection) > 1:
            writeline('Case #%d: Bad magician!' % i)
        else:
            writeline('Case #%d: %d' % (i, list(intersection)[0]))

if __name__ == '__main__':
    magic(sys.stdin, sys.stdout)
