#!/usr/bin/env python3

import sys
import re
import heapq

def read():
    return sys.stdin.readline().strip()

def add_person(occupancy, gap_heap):
    max_gap_size, gap_left = heapq.heappop(gap_heap)
    max_gap_size = -max_gap_size

    index = gap_left + (max_gap_size-1)//2
    occupancy[index] = 1

    new_gap1 = (max_gap_size-1)//2
    new_gap2 = max_gap_size//2

    # add the new gaps to the heap
    heapq.heappush(gap_heap, (-new_gap1, gap_left))
    heapq.heappush(gap_heap, (-new_gap2, index+1))

    return index

def calculate_gaps(occupancy, index):
    gaps = []
    for direction in (1, -1):
        count = 0
        i = index + direction
        while occupancy[i] == 0:
            i += direction
            count += 1
        gaps.append(count)
    return gaps

def main():
    num_cases = int(read())
    for i in range(num_cases):
        n, k = [int(x) for x in read().split(" ")]
        occupancy = [1] + [0] * n + [1]
        gap_heap = [(-n, 1)]

        for _ in range(k):
            stall = add_person(occupancy, gap_heap)

        gaps = calculate_gaps(occupancy, stall)
        print("Case #{}: {} {}".format(i+1, max(gaps), min(gaps)))
        sys.stdout.flush()

if __name__ == '__main__':
    main()

