#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        cakes, k = sys.stdin.readline().strip().split()
        cakes = list(cakes)
        k = int(k)
        cnt = 0
        for j in range(0, len(cakes) - k + 1):
            if cakes[j] == '-':
                cnt += 1
                for l in range(j + 1, j + k):
                    if cakes[l] == '+':
                        cakes[l] = '-'
                    else:
                        cakes[l] = '+'
        for j in range(len(cakes) - k + 1, len(cakes)):
            if cakes[j] == '-':
                print('Case #{}: IMPOSSIBLE'.format(i + 1))
                break
        else:
            print('Case #{}: {}'.format(i + 1, cnt))

if __name__ == '__main__':
    main()
