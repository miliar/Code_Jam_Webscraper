import heapq
import sys


class MaxHeap(object):
    def __init__(self):
        self.q = []

    def push(self, x):
        heapq.heappush(self.q, -x)

    def pop(self):
        return -heapq.heappop(self.q)

    @property
    def size(self):
        return len(self.q)


def max_size_at_step(initial_size, step):
    heap = MaxHeap()
    heap.push(initial_size)
    for i in xrange(1, step):
        max_item = heap.pop()
        if max_item == 1:
            continue
        elif max_item == 2:
            heap.push(1)
        elif max_item % 2 == 0:
            heap.push(max_item / 2)
            heap.push(max_item / 2 - 1)
        else:
            heap.push(max_item / 2)
            heap.push(max_item / 2)
    return -heap.q[0]


def stalls(size, steps):
    last_step = max_size_at_step(size, steps)
    if last_step == 1:
        return 0, 0
    elif last_step == 2:
        return 1, 0
    elif last_step % 2 == 0:
        return last_step / 2, last_step / 2 - 1
    else:
        return last_step / 2, last_step / 2


def solve_from_input():
    case_count = int(sys.stdin.readline().strip())
    for i in xrange(1, case_count + 1):
        size, steps = map(int, sys.stdin.readline().strip().split())
        l, r = stalls(size, steps)
        sys.stdout.write('Case #{}: {} {}\n'.format(i, l, r))


if __name__ == '__main__':
    solve_from_input()
