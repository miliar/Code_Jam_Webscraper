from heapq import heappush, heappop
from collections import deque
import fileinput


class MaxMergeHeap(object):

    def __init__(self):
        self.heap = []
        self.map = {0: 42}

    def push(self, node):
        if node[0] == 0:
            return
        val, count = node
        if val in self.map:
            self.map[val] += count
        else:
            self.map[val] = count
            heappush(self.heap, - val)

    def pop(self):
        val = - heappop(self.heap)
        count = self.map.pop(val)

        left = (val - 1) >> 1
        right = val - left - 1

        self.push([left, count])
        self.push([right, count])

    def top(self):
        val = - self.heap[0]
        return self.map[val]


def solve(pool):
    interval = - pool.heap[0]
    left = (interval - 1) >> 1
    right = interval - left - 1
    return max(left, right), min(left, right)


def deduce(pool, num):
    # print pool.heap, pool.q
    count = pool.top()
    if count > num:
        return solve(pool)
    if count == num:
        pool.pop()
        pool.map.pop(- pool.heap[0])
        return solve(pool)

    pool.pop()
    return deduce(pool, num - count)


def magic(n, k):
    pool = MaxMergeHeap()
    pool.push([n, 1])
    return deduce(pool, k - 1)

f = fileinput.input()
cases = int(f.readline().strip())
for case in range(cases):
    n, k = map(int, f.readline().strip().split())
    result = magic(n, k)
    print "Case #{}: {} {}".format(case + 1, result[0], result[1])
