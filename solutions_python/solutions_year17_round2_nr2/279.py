#!/usr/bin/env python3

import sys

from collections import Counter
from copy import deepcopy

colors = {
    'R': ['R'],
    'O': ['R', 'O'],
    'Y': ['Y'],
    'G': ['Y', 'B'],
    'B': ['B'],
    'V': ['B', 'R']
}

####################################################################
#                           Helpers                                #
####################################################################


def read_int():
    return int(input())


def read_ints():
    return [int(s) for s in input().split()]


####################################################################
#                           Solution                               #
####################################################################

def case(n, r, o, y, g, b, v, n_red, n_yellow, n_blue):
    counts = {
        'R': n_red,
        'Y': n_yellow,
        'B': n_blue
    }
    remaining = {
        'R': [['R'], r],
        'O': [['R', 'Y'], o],
        'Y': [['Y'], y],
        'G': [['Y', 'B'], g],
        'B': [['B'], b],
        'V': [['B', 'R'], v]
    }

    with_color = {
        'R': ['R', 'O', 'V'],
        'B': ['B', 'V', 'G'],
        'Y': ['Y', 'O', 'G']
    }

    first = None
    # pick random
    for k in remaining:
        if remaining[k][1] != 0:
            first = k
            break

    solution = [first]
    for c in remaining[first][0]:
        counts[c] -= 1
        assert counts[c] >= 0
    remaining[first][1] -= 1
    assert remaining[first][1] >= 0

    while len(solution) < n:
        cnts = counts.copy()
        for c in remaining[first][0]:
            cnts[c] += 0.5

        for c in remaining[solution[-1]][0]:
            cnts[c] = -1  # do not choose incompatible with last chosen

        # color has to be there
        col = max(cnts.items(), key=lambda x: x[1])[0]

        # among those choose with highest priority
        priority = {}

        for k, (cols, cnt) in remaining.items():
            if remaining[k][1] > 0 and col in cols and len(set(cols) & set(remaining[solution[-1]][0])) == 0:
                p = len(cols) * 1000000 - cnt
                if col in remaining[first][0]:
                    p -= 1
                priority[k] = p
            else:
                priority[k] = float('-inf')

        k = max(priority.items(), key=lambda x: x[1])[0]
        assert priority[k] > -1000

        solution.append(k)
        for c in remaining[k][0]:
            counts[c] -= 1
        remaining[k][1] -= 1

    # check
    counts = Counter(solution)
    assert counts['R'] == r
    assert counts['Y'] == y
    assert counts['B'] == b
    assert solution[-1] != solution[0]

    assert len(solution) == n
    return ''.join(solution)



####################################################################
#                              I/O                                 #
####################################################################

def main():
    ################################################################
    # Define input and output
    #in_file_name = 'example.in'
    in_file_name = 'B-small-attempt1.in'
    #in_file_name = 'B-large.in'
    out_file_name = in_file_name.rstrip('.in') + '.out'
    # will be closed by garbage collector
    orig_stdout = sys.stdout
    sys.stdin = open(in_file_name)
    sys.stdout = open(out_file_name, "w")
    ################################################################

    for i in range(read_int()):
        x = read_ints()
        n, r, o, y, g, b, v = x
        n_red = r + o + v
        n_yellow = y + o + g
        n_blue = b + g + v

        limit = n / 2
        if n_red > limit or n_yellow > limit or n_blue > limit:
            solution = 'IMPOSSIBLE'
        else:
            solution = case(n, r, o, y, g, b, v, n_red, n_yellow, n_blue)
        print(".", file=orig_stdout, end='')
        print("Case #%s: %s" % (i+1, solution))
    print("\nsaved to %s" % out_file_name, file=orig_stdout, end='')


if __name__ == '__main__':
    main()
