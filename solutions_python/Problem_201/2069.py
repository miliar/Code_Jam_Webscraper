import sys
import heapq
from collections import deque

class Stall:
    def __init__(self, x):
        self.left  = None
        self.right = None
        self.x     = x
        self.empty = True

    @property
    def min(self):
        return min(abs(self.x-self.left.x), abs(self.x-self.right.x)) - 1

    @property
    def max(self):
        return max(abs(self.x-self.left.x), abs(self.x-self.right.x)) - 1

    def __repr__(self):
        return '.' if self.empty else '0'

    def __lt__(self, other):
        if(self.min > other.min):
            return True
        if(self.min < other.min):
            return False
        if(self.max > other.max):
            return True
        if(self.max < other.max):
            return False
        return self.x < other.x


def solve1(n, k):
    if (n == k):
        return (0, 0)
    n += 2
    stalls = [Stall(x) for x in range(0, n)]
    for s in stalls:
        s.left  = stalls[0]
        s.right = stalls[-1]
    stalls[0].empty = False
    stalls[-1].empty = False
    empty  = [stalls[i] for i in range(1, n - 1)]
    for i in range(k):
        heapq.heapify(empty)
        best = heapq.heappop(empty)
        best.empty = False
        for j in range(best.left.x + 1, best.x):
            stalls[j].right = best
        for j in range(best.x + 1, best.right.x):
            stalls[j].left = best
    return (best.max, best.min)

def solve2(n, k):
    if (n == k):
        return (0, 0)
    # r = ['0'] + ['.'] * n + ['0']
    queue = [(n + 1, 0, n + 1)]
    for i in range(k):
        l, a, b = heapq.heappop(queue)
        m = (a + b) // 2
        # r[m] = '0'
        if ((m - a) > 1):
            heapq.heappush(queue, (a - m, a, m))
        if ((b - m) > 1):
            heapq.heappush(queue, (m - b, m, b))
        # print(''.join(r))
    return max(m - a, b - m) - 1, min(m - a, b - m) - 1


def solve(n, k):
    return solve2(n, k)


def read_input():
    t = int(input())
    for i in range(t):
        sys.stderr.write('Reading {} out of {}\n'.format(i + 1, t))
        n, k = map(int, input().split())
        yield n, k


def main():
    results = [solve(*test_case) for test_case in read_input()]
    for i, result in enumerate(results):
        print (
            "Case #{}: {}".format(
                i + 1,
                ' '.join(str(x) for x in result)
            )
        )
if __name__ == '__main__':
    main()