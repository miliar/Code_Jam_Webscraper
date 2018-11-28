#!/usr/bin/env python3
import sys

#sys.stdin = open('A-sample.in', 'r')
#sys.stdout = open('A-sample.out', 'w')

for c in range(1, int(input()) + 1):

    D, N = map(int, input().strip().split(' '))

    T = 0
    for i in range(N):
        P, S = map(int, input().strip().split(' '))
        T = max(T, (D-P)/S)
    print('Case #%s: %.6f' % (c, D/T))
