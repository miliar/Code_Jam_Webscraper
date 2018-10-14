"""
Code Jam 2017
Qualification Round
Problem C - Bathroom Stalls

Author: Ben Feinstein
"""
from __future__ import print_function, division

# noinspection PyCompatibility
from queue import PriorityQueue


class SmartQueue:
    def __init__(self):
        self._heap = PriorityQueue()  # use (-n) because it's a MinHeap
        self._dict = dict()

    def put(self, n, k):
        if n in self._dict:
            self._dict[n] += k
        else:
            _n = -n
            self._heap.put(_n)
            self._dict[n] = k

    def pop(self):
        assert not self._heap.empty(), "can't pop when empty"
        _n = self._heap.get()
        n = -_n
        k = self._dict[n]
        return n, k


def split_interval(n):
    l_min = (n - 1) // 2
    l_max = (n - 1) - l_min
    return l_max, l_min


def assign_stalls(stalls, men):
    queue = SmartQueue()
    queue.put(stalls, 1)
    while True:
        n, k = queue.pop()
        l_max, l_min = split_interval(n)

        if k >= men:
            return l_max, l_min

        if l_max > 0:
            queue.put(n=l_max, k=k)
        if l_min > 0:
            queue.put(n=l_min, k=k)

        men -= k


def main():
    n_tests = int(input())
    for test_case in range(1, n_tests + 1):
        stalls, men = [int(x) for x in input().split()]
        l_max, l_min = assign_stalls(stalls, men)
        print("Case #{test_case:d}: {l_max:d} {l_min:d}".format(test_case=test_case,
                                                                l_max=l_max, l_min=l_min))


if __name__ == '__main__':
    main()
