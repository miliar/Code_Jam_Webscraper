#-*-coding:utf-8-*-

import os, sys, re

fh = open(sys.argv[1])
T = int(fh.readline())

for i in range(T):
    N, K = [int(x.strip()) for x in fh.readline().split(' ')]
    n = 2 ** N - 1
    if (K & n) == n:
        print('Case #%d: ON' % (i + 1))
    else:
        print('Case #%d: OFF' % (i + 1))
        pass
    pass
