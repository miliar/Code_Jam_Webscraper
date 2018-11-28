#!/usr/bin/env python

import sys

class MovingQueue(object):
    """Circular queue.

    >>> q = MovingQueue(range(10))
    >>> list(q)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> q.advance(1)
    >>> q[0]
    1
    >>> q[len(q) - 1]
    0
    >>> q[len(q)]
    Traceback (most recent call last):
    ...
    KeyError: 'Index out of range'
    >>> q.original(0)
    1

    """

    def __init__(self, queue):
        self.offset = 0
        self.queue = queue
        self.len = len(queue)

    def __len__(self):
        return self.len

    def __getitem__(self, index):
        if 0 <= index < self.len:
            return self.queue[self.original(index)]
        raise KeyError("Index out of range")

    def __iter__(self):
        for i in xrange(self.len):
            yield self[i]

    def advance(self, offset):
        self.offset += offset
        self.offset %= self.len

    def original(self, index=0):
        """Index in original list."""
        index += self.offset
        return index % self.len

def solve(runs, limit, groups):
    """

    >>> solve(4, 6, [1, 4, 2, 1])
    21
    >>> solve(10, 6, [1, 4, 2, 1])
    21
    >>> solve(100, 10, [1])
    100
    >>> solve(5, 5, [2, 4, 2, 3, 4, 2, 1, 2, 1, 3])
    20

    """
    q = MovingQueue(groups)
    # to detect length of the cycle
    last_seen = dict()
    total = 0

    r = 0
    while r < runs:
        sum = 0
        start = q.original()
        # Cycle detection
        if start in last_seen:
            # So we have a cycle that gives cycle_income per cycle_runs
            before_runs, before_income = last_seen[start]
            cycle_runs, cycle_income = r - before_runs, total - before_income
            left_runs = runs - r
            if left_runs > cycle_runs:
                cycles = left_runs / cycle_runs
                total += cycles * cycle_income
                r += cycles * cycle_runs
                continue
        else:
            last_seen[start] = (r, total)

        # Naive, take as much groups as we can
        for i in range(len(q)):
            if sum + q[i] > limit:
                break
            else:
                sum += q[i]
        q.advance(i)
        total += sum
        r += 1
    return total


def input(fp=sys.stdin):
    T = int(fp.readline())
    for t in range(T):
        R, k, _ = map(int, fp.readline().split())
        g = map(int, fp.readline().split())
        ans = solve(R, k, g)
        print 'Case #%d: %s' % (t+1, ans)

if __name__ == '__main__':
    if '--test' in sys.argv:
        import doctest
        doctest.testmod()
    else:
        input()

