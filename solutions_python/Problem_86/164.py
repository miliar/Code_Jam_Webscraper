#!/usr/bin/env python

import sys
from functools import reduce

#def gcd(a, b):
#    if b == 0:
#        return a
#    return gcd(b, a % b)
#
#def lcd(a, b):
#    return (a * b)/gcd(a, b)

def harmony(notes, l, h):
    if l == 1:
        return l
    for i in range(l, h + 1):
        divide = True
        for note in notes:
            if note > i and note % i != 0 or (i > note and i % note != 0):
                divide = False
                continue
        if divide:
            return i
    return 'NO'

if __name__ == '__main__':
    ncases = int(sys.stdin.readline())
    for i in range(ncases):
        n, l, h = [int(x) for x in sys.stdin.readline().split()]
        notes = [int(x) for x in sys.stdin.readline().split()]
        print('Case #', i + 1, ': ', harmony(notes, l, h), sep='')
