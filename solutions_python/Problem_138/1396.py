#!/usr/bin/env python
import sys

def readline():
    return sys.stdin.readline()

def readreal():
    return float(readline())

def readreals():
    return [float(x) for x in readline().strip().split()]

def readint():
    return int(readline())

def readints():
    return [int(x) for x in readline().strip().split()]

def deceit(cnt, n, k):
    np = 0
    dw = (1.0 - k[-1]) / (cnt + 1)
    bluff = k[-1] + dw
    while n:
        if (len(n) < 2):
            N = n.pop(0)
        else:
            N = None
            for i, NN in enumerate(n):
                if NN > k[0]:
                    del n[i]
                    N = bluff
                    bluff += dw
                    break
            if N is None:
                del n[0]
                N = (k[-1] + k[-2]) / 2.0
        naomi_wins = True
        for K in k:
            if K > N:
                k.remove(K)
                naomi_wins = False
                break
        if naomi_wins:
            del k[0]
            np += 1
    return np

def war(cnt, n, k):
    np = 0
    n.reverse()
    for N in n:
        naomi_wins = True
        for K in k:
            if K > N:
                k.remove(K)
                naomi_wins = False
                break
        if naomi_wins:
            del k[0]
            np += 1
    return np

def read_case():
    blocks = readint()
    n = readreals()
    n.sort()
    k = readreals()
    k.sort()
    return '{0} {1}'.format(deceit(blocks, n[:], k[:]), war(blocks, n, k))

def main():
    cases = readint()
    for c in range(1, cases + 1):
        print 'Case #{0:d}: {1}'.format(c, read_case())

if __name__ == '__main__':
    main()

