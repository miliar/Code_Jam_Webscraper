#!/usr/bin/env python3
# performance run: pypy3 -uOO run.py

import heapq

class MaxHeap:
    def __init__(self): self.heap = []
    def push(self, x): heapq.heappush(self.heap, -x)
    def pop(self): return -heapq.heappop(self.heap)
    def __getitem__(self, i): return -self.heap[i]
    def __len__(self): return len(self.heap)
    def __str__(self): return self.heap.__str__()

def step(heap):
    largest = heap.pop()
    l = (largest-1)//2
    r = largest//2

    heap.push(l)
    heap.push(r)

def step_last(heap):
    largest = heap.pop()
    l = (largest-1)//2
    r = largest//2

    y = max(l, r)
    z = min(l, r)

    return (y, z)

def solve(n, k):
    h = MaxHeap()
    h.push(n)

    for _ in range(k-1):
        step(h)
    y, z = step_last(h)

    return '{} {}'.format(y, z)

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        line = input()
        N, K = [int(x) for x in line.split()]
        result = solve(N, K)
        print('Case #{}: {}'.format(i+1, result))
