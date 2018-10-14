#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import heapq

def do_it(n, k):
    heap = [-n]
    for _ in xrange(k):
        item = -heapq.heappop(heap)
        item -= 1
        l1 = l2 = item/2
        if item % 2 != 0:
            l1 += 1
        if l1 != 0:
            heapq.heappush(heap, -l1)
        if l2 != 0:
            heapq.heappush(heap, -l2)
    return l1, l2


def main():
    cases = int(next(sys.stdin).strip())
    for num in xrange(1, cases+1):
        n, k = map(int, next(sys.stdin).strip().split())
        print 'Case #{}: {} {}'.format(num, *do_it(n, k))


if __name__ == '__main__':
    main()
