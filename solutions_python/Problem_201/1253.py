#!/usr/bin/python3

import re

def add_count(counts, num_rooms, num_count):
    if num_rooms in counts:
        counts[num_rooms] += num_count
    else:
        counts[num_rooms] = num_count

def split_rooms(num_rooms):
    assert num_rooms > 0
    num_rooms -= 1
    if num_rooms % 2 == 1:
        left = (num_rooms - 1) // 2
        right = (num_rooms + 1) // 2
    else:
        left = num_rooms // 2
        right = num_rooms // 2
    return left, right

def solve(N, K):
    counts = {N: 1}

    batch = 1
    remain = K
    while batch < remain:
        new_counts = {}
        for num in counts:
            left, right = split_rooms(num)
            if left > 0:
                add_count(new_counts, left, counts[num])
            if right > 0:
                add_count(new_counts, right, counts[num])
        counts = new_counts
        remain -= batch
        batch *= 2

    finals = list(counts.keys())
    if len(finals) == 1:
        left, right = split_rooms(finals[0])
    elif len(finals) == 2:
        more = max(finals)
        less = min(finals)
        if remain <= counts[more]:
            left, right = split_rooms(more)
        else:
            left, right = split_rooms(less)
    else:
        assert False

    return max(left, right), min(left, right)

def main():
    T = int(input())

    for idx in range(T):
        line = input()
        tokens = re.split(' ', line)
        N = int(tokens[0])
        K = int(tokens[1])

        result = solve(N, K)

        a = '{} {}'.format(*result)
        print('Case #{}: {}'.format(idx + 1, a))

if __name__ == '__main__':
    main()
