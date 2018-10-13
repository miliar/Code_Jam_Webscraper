import StringIO
import itertools
import math

from collections import defaultdict

from ecodejam.input_parser import *
import heapdict


class MaxHeap(object):
    def __init__(self, values=[]):
        self.counter = 0

        self.heap = heapdict.heapdict()
        for value in values:
            self.add(value)

    def add(self, value):
        self.counter += 1
        self.heap[self.counter] = -value

    def peek(self):
        return -self.heap.peekitem()[1]

    def pop(self):
        return -self.heap.popitem()[1]

    def __len__(self):
        return len(self.heap)


def solve_small(case_index):
    n = read_int()
    k = read_int()
    next_line()

    stalls = [1] + [0] * n + [1]

    max_ls_rs = 0
    min_ls_rs = 0

    for i in xrange(k):
        # First, find the largest, and leftmost gap
        max_gap_size = 0
        max_gap_start = 0

        cur_gap_size = 0
        cur_gap_start = 0

        for i in xrange(len(stalls)):
            if stalls[i] == 0:
                cur_gap_size += 1
            else:
                if cur_gap_size > max_gap_size:
                    max_gap_size = cur_gap_size
                    max_gap_start = cur_gap_start
                cur_gap_start = i + 1
                cur_gap_size = 0

        # Then choose the middle cell of the largest gap
        stalls[max_gap_start + (max_gap_size - 1) / 2] = 1

        # Calculate max(LS, RS), min(LS, RS)
        ls = int(math.floor((max_gap_size - 1) * 1.0 / 2))
        rs = int(math.ceil((max_gap_size - 1) * 1.0 / 2))
        max_ls_rs = max(ls, rs)
        min_ls_rs = min(ls, rs)

    return str(max_ls_rs) + " " + str(min_ls_rs)


def solve_better(case_index):
    n = read_int()
    k = read_int()
    next_line()

    gaps = [n]

    max_ls_rs = 0
    min_ls_rs = 0

    for i in xrange(k):
        # First, find the largest, and leftmost gap
        max_gap_index = max(xrange(len(gaps)), key=lambda i: gaps[i])
        max_gap_size = gaps[max_gap_index]

        effective_gap_size = max_gap_size - 1

        if effective_gap_size & 1 == 0:
            rs = ls = effective_gap_size / 2
        else:
            ls = effective_gap_size / 2
            rs = ls + 1

        gaps = gaps[:max_gap_index] + [
            ls,
            rs
        ] + gaps[max_gap_index + 1:]

        # Calculate max(LS, RS), min(LS, RS)

        max_ls_rs = max(ls, rs)
        min_ls_rs = min(ls, rs)

    return str(max_ls_rs) + " " + str(min_ls_rs)


def solve_better2(case_index):
    # print case_index
    n = read_int()
    k = read_int()
    next_line()

    gaps = MaxHeap([n])

    max_ls_rs = 0
    min_ls_rs = 0

    # dbg_gap_sizes = defaultdict(lambda: 0)

    for i in xrange(k):
        # First, find the largest, and leftmost gap
        max_gap_size = gaps.pop()
        # dbg_gap_sizes[max_gap_size] += 1

        effective_gap_size = max_gap_size - 1

        if effective_gap_size & 1 == 0:
            rs = ls = effective_gap_size / 2
        else:
            ls = effective_gap_size / 2
            rs = ls + 1

        if ls > 0:
            gaps.add(ls)
        if rs > 0:
            gaps.add(rs)

        # Calculate max(LS, RS), min(LS, RS)

        max_ls_rs = max(ls, rs)
        min_ls_rs = min(ls, rs)

    # print "*****"
    # for i in sorted(dbg_gap_sizes.keys(), reverse=True):
    #     print i, "-", dbg_gap_sizes[i]
    # print "*****"

    return str(max_ls_rs) + " " + str(min_ls_rs)


def solve_better3(case_index):
    n = read_int()
    k = read_int()
    next_line()

    room_left = n
    phase_count = 1
    k_index = 1

    while True:
        # high = room_left - (room_left / phase_count) * phase_count
        # low = phase_count - high
        # print "high:", (room_left / phase_count) + 1, "-", high
        # print "low:", (room_left / phase_count), "-", low

        if k_index <= k < k_index + phase_count:
            high = room_left - (room_left / phase_count) * phase_count
            low = phase_count - high

            print "high:", (room_left / phase_count) + 1, " - ", high
            print "low:", (room_left / phase_count), " - ", low

            if k < k_index + high:
                span_for_k = (room_left / phase_count) + 1
            else:
                span_for_k = (room_left / phase_count)

            effective_gap_size = span_for_k - 1

            if effective_gap_size & 1 == 0:
                rs = ls = effective_gap_size / 2
            else:
                ls = effective_gap_size / 2
                rs = ls + 1

            max_ls_rs = max(ls, rs)
            min_ls_rs = min(ls, rs)

            return str(max_ls_rs) + " " + str(min_ls_rs)

        room_left -= phase_count
        k_index += phase_count
        phase_count *= 2


solve = solve_better3


SAMPLE = """
5
4 2
5 2
6 2
1000 1000
1000 1
"""


if __name__ == "__main__":
    set_parsed_input(
        StringIO.StringIO(SAMPLE)
    )
    run_solver(solve)
