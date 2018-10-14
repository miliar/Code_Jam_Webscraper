#!/usr/bin/python

# google code jam - c.durr - 2009
# Welcome to code Jam
# dyn. progr. A[i][j] = number of times sustring w[:i] apears in s[:j]
# modulo 10000

import sys

N = int(sys.stdin.readline())
w = "welcome to code jam"

for test in range(N):
    s = sys.stdin.readline().strip()
    A = [[0 for j in range(len(s)+1)] for i in range(len(w)+1)]
    for i in range(len(w)+1):
        for j in range(len(s)+1):
            if i==0:
                A[i][j] = 1
            elif j==0:
                A[i][j] = 0
            else:
                if w[i-1]==s[j-1]:
                    A[i][j] = (A[i][j-1]+A[i-1][j-1])%1000
                else:
                    A[i][j] = A[i][j-1]

    print 'Case #%d: %04d' % (test+1, A[len(w)][len(s)])
