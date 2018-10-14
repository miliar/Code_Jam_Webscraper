#!/usr/bin/env python3

import os


def main(pattern, k):
    """
    Returns number of flips
    """
    count = 0
    pancake_seq = list(pattern)
    while pancake_seq and len(pancake_seq) >= k:
        pancake_seq = remove_first_up_cakes(pancake_seq)
        if len(pancake_seq) >= k:
            count += 1
            _flip(pancake_seq, k)

    return count if not pancake_seq else "IMPOSSIBLE"


def remove_first_up_cakes(pancake_seq):
    i = 0
    while i < len(pancake_seq) and pancake_seq[i] == '+':
        i += 1
    return pancake_seq[i:]


def _flip(pancake_seq, k):
    for i in range(k):
        pancake_seq[i] = "+" if pancake_seq[i] == '-' else '-'


if __name__ == '__main__':
    with open(os.path.expanduser("~/Downloads/A-small-attempt0.in")) as fd:
        t = int(fd.readline())
        for i in range(1, t + 1):
            pattern, m = fd.readline().strip().split()
            m = int(m)
            if '-' not in pattern:
                print("Case #{}: {}".format(i, 0))
            else:
                r = main(pattern, m)
                print("Case #{}: {}".format(i, r))
