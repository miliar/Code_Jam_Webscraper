import sys


T = int(input())
for testno in xrange(1, T + 1):
    N = int(sys.stdin.readline())
    C = map(int, sys.stdin.readline().split())
    X = 0
    Sum = 0
    for c in C:
        X ^= c
        Sum += c

    Sum -= min(C)

    res = 'NO'
    if X == 0:
        res = str(Sum)

    print 'Case #{0}: {1}'.format(testno, res)
