#!/usr/bin/env python

import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        N = int(sys.stdin.readline())
        M = list(map(int, sys.stdin.readline().split()))

        diff = [M[j] - M[j + 1] for j in range(N - 1)]
        max_eaten = max(diff)

        count_1 = sum(x for x in diff if x > 0)
        count_2 = sum(min(max_eaten, M[j]) for j in range(N - 1))

        print('Case #%d: %d %d' % (i + 1, count_1, count_2))