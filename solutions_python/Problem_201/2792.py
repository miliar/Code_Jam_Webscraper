import sys
from itertools import groupby, takewhile

from typing import List

from common.cases import write_cases_to_file

input = (line.strip().split(' ') for line in sys.stdin if line.strip())
next(input)
# input = [(sys.argv[1], sys.argv[2])]


def find_isolated_stall(stalls: List[int]):
    chosen = -1, 3  # idx, min_length
    i = 0
    while i < len(stalls):
        if stalls[i] == 0:
            unoccupied_stalls = list(takewhile(lambda x: x == 0, stalls[i:]))
            if len(unoccupied_stalls) >= chosen[1]:
                middle_stall = int(((len(unoccupied_stalls) - 1) / 2))
                chosen = (i + middle_stall), len(unoccupied_stalls)
            i += len(unoccupied_stalls)
        i += 1
    return chosen


def find_largest_distance(stalls: List[int]):
    chosen = -1, 0  # idx, len
    i = 0
    while i < len(stalls):
        if stalls[i] == 0:
            unoccupied_stalls = list(takewhile(lambda x: x == 0, stalls[i:]))
            if len(unoccupied_stalls) > chosen[1]:
                chosen = i, len(unoccupied_stalls)
            i += len(unoccupied_stalls)
        i += 1
    return chosen


cases = []
for n, k in input:
    n = int(n)
    k = int(k)
    stalls = [1] + [0] * n + [1]
    for i in range(k):
        min_idx, min_length = find_isolated_stall(stalls)
        max_idx, max_length = find_largest_distance(stalls)
        if min_idx != -1:
            stalls[min_idx] = 1
        elif max_idx != -1:
            stalls[max_idx] = 1
    output_max = int(max_length / 2) if max_idx != -1 else 0
    output_min = min(
        [(min_length - 1 - int(((min_length - 1) / 2))),
         (int(((min_length - 1) / 2)))]
    ) if min_idx != -1 else 0
    cases.append("%d %d" % (output_max, output_min))

write_cases_to_file(cases, 'bathroom.txt')
