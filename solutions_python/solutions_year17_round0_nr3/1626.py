from __future__ import print_function

import fractions
import heapq
import sys

def calc(N, K):
    heap = []
    heapq.heappush(heap, (-N, 0))  # (-len, pos) to make it max heap.
    n1, n2 = -1, -1
    for i in xrange(K):
        n, p = heapq.heappop(heap)
        n = abs(n)
        h = n // 2
        if n % 2 == 0:
            n1 = h - 1
            n2 = h
        else:
            n1 = h
            n2 = h
        if n1 > 0:
            heapq.heappush(heap, (-n1, p))
        if n2 > 0:
            heapq.heappush(heap, (-n2, p + n1 + 1))
    return max(n1, n2), min(n1, n2)

def main():
    f = sys.stdin

    if len(sys.argv) > 1:
        f = open(sys.argv[1], "rt")

    T = int(f.readline().strip())

    for case_id in range(1, T+1):
        N, K = map(int, f.readline().strip().split())
        assert 1 <= K <= N, '{} {}'.format(K, N)

        r = calc(N, K)

        print('Case #{}: {} {}'.format(case_id, r[0], r[1]))

def do_stuff():
    print(calc(4, 3))

if __name__ == '__main__':
    main()
    # do_stuff()
