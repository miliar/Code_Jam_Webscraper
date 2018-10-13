#!/usr/bin/env python
import sys

def readline():
    return sys.stdin.readline()

def readint():
    return int(readline())

def readints():
    return [int(x) for x in readline().strip().split()]

def readrows():
    return [readints() for i in range(4)]

def read_case():
    a1 = readint() - 1
    row1 = readrows()[a1]
    a2 = readint() - 1
    row2 = readrows()[a2]
    r = [x for x in row1 for y in row2 if x == y]
    if len(r) == 1:
        return str(r[0])
    if len(r) == 0:
        return 'Volunteer cheated!'
    return 'Bad magician!'

def main():
    cases = readint()
    for c in range(1, cases + 1):
        print 'Case #{0}: {1}'.format(c, read_case())

if __name__ == '__main__':
    main()

