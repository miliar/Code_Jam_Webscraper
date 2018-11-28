#!/usr/bin/python
import string, sys

nr = string.atoi(sys.stdin.readline().strip())
for i in range(nr):
    N, K = map(lambda x: string.atoi(x), sys.stdin.readline().strip().split())
    val = (1 << N) - 1
    res = ((K & val) == val)
    print 'Case #%d: %s' % (i + 1, ('OFF', 'ON')[res])
