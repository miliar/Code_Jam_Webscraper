from sys import stdin
#import bisect as bs
#import collections as co
#import heapq
#import itertools as it
#import math
#import re
#import string

DEBUG = True
INF = 2000000000 #2 billion
EPS = 1e-9

def line():
    return stdin.readline().strip()


def main():
    cases = int(line())
    for case in range(cases):
        n = int(line())
        seq = map(int, line().split())
        best = 0

        for take in range(1, 2 ** n - 1):
            p1, p2 = 0, 0
            real_val = 0

            for i in range(n):
                if take & (1 << i):
                    p1 ^= seq[i]
                    real_val += seq[i]
                else:
                    p2 ^= seq[i]

            if p1 == p2:
                best = max(best, real_val)

        print 'Case #%d: %s' % (case + 1, best or 'NO')


if __name__ == '__main__':
    if DEBUG:
        stdin = open('input.txt')
    main()
