#!/usr/bin/env python

from pprint import pprint


def task(A, B, K):
    count = 0
    A, B = min(A, B), max(A, B)
    for b in xrange(B):
        for a in xrange(A):
            if a & b < K:
                count += 1
    return count


def main():
    T = int(raw_input())
    for index in xrange(T):
        print 'Case #%d: %s' % (index + 1, task(*map(int, raw_input().split())))


if __name__ == '__main__':
    main()
