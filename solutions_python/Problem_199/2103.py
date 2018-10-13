#!/usr/bin/env python3
import sys

#sys.stdin = open('A-sample.in', 'r')
#sys.stdout = open('A-sample.out', 'w')

for c in range(1, int(input()) + 1):

    s, n = input().strip().split(' ')
    n = int(n)
    a = list(s)
    m = 0
    for i in range(len(a)-n+1):
        if a[i] == '-':
            m += 1
            for j in range(n):
                a[i+j] = '-' if a[i+j] == '+' else '+'
        #print(''.join(a))
    if '-' in ''.join(a):
        m = 'IMPOSSIBLE'
    print('Case #%s: %s' % (c, m))
