#!/usr/bin/env python3

from collections import namedtuple
import fileinput
import heapq


freestalls = namedtuple('freestalls', ['neg_min', 'neg_max', 'x', 'n'])


def distances(n):
    middle = (n-1) // 2
    return middle, n-middle-1


def test_distances():
    assert distances(1) == (0, 0)
    assert distances(2) == (0, 1)
    assert distances(3) == (1, 1)
    assert distances(4) == (1, 2)


def make_freestalls(x, n):
    ls, rs = distances(n)
    return freestalls(-min(ls, rs), -max(ls, rs), x, n)


def solve(N, K):
    freelist = []
    heapq.heappush(freelist, make_freestalls(0, N))

    for i in range(K):
        #print(i, 'freelist', freelist)
        block = heapq.heappop(freelist)
        x = block.x + (block.n-1)//2
        #print('take', x)
        
        n_left = -block.neg_min # x - block.x
        if n_left > 0:
            heapq.heappush(freelist, make_freestalls(block.x, n_left))
        
        n_right = -block.neg_max #block.n - x - 1
        if n_right > 0:
            heapq.heappush(freelist, make_freestalls(x+1, n_right))

    return -block.neg_min, -block.neg_max


def main():
    cases = int(input())
    for i, line in enumerate(fileinput.input()):
        n, k = line.split()
        minlr, maxlr = solve(int(n), int(k))
        print('Case #{}: {} {}'.format(i+1, maxlr, minlr))

    assert i == cases-1, 'read wrong number of cases'


if __name__ == '__main__':
    main()
