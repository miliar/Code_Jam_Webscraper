#!/usr/bin/env python3.4
import sys
import math

if __name__ == '__main__':
    for testCase in range(int(sys.stdin.readline())):
        length = int(sys.stdin.readline())
        pieces = list(map(int, sys.stdin.readline().split()))
        firstMethod = 0
        for i in range(1, length):
            if pieces[i] < pieces[i - 1]:
                firstMethod += pieces[i - 1] - pieces[i]
        diff = []
        for i in range(1, length):
            diff.append(pieces[i - 1] - pieces[i])
        speed = max(diff)
        secondMethod = 0
        for i in range(length - 1):
            if pieces[i] < speed:
                secondMethod += pieces[i]
            else:
                secondMethod += speed
        print('Case #%d: %d %d' % (testCase + 1, firstMethod, secondMethod))
