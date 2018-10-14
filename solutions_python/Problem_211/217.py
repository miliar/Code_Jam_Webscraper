#!/usr/bin/env python3

import sys

from collections import Counter

####################################################################
#                           Helpers                                #
####################################################################


def read_int():
    return int(input())


def read_ints():
    return [int(s) for s in input().split()]


def read_float():
    return float(input())


def read_floats():
    return [float(s) for s in input().split()]


####################################################################
#                           Solution                               #
####################################################################


def case(p, u):
    p = sorted(p)
    p.append(1.0)
    i = 0
    while u > 0.000000001:
        if len(p) < i + 2:
            break
        diff = p[i+1] - p[i]
        max_diff = u / (1.0 + i)
        diff = min(max_diff, diff)
        u -= diff * (1.0 + i)
        if diff > 0.000000001:
            for i in range(i+1):
                p[i] += diff
        i += 1

    for i in range(len(p)):
        p[i] = min(1.0, p[i])
    prod = 1
    for el in p:
        prod *= el
    return prod



####################################################################
#                              I/O                                 #
####################################################################

def main():
    ################################################################
    # Define input and output
    #in_file_name = 'example.in'
    in_file_name = 'C-small-1-attempt0.in'
    #in_file_name = 'C-large.in'
    out_file_name = in_file_name.rstrip('.in') + '.out'
    # will be closed by garbage collector
    orig_stdout = sys.stdout
    sys.stdin = open(in_file_name)
    sys.stdout = open(out_file_name, "w")
    ################################################################

    for i in range(read_int()):
        n, k = read_ints()
        u = read_float()
        p = read_floats()
        solution = case(p, u)
        print(".", file=orig_stdout, end='')
        print("Case #%s: %s" % (i+1, solution))
    print("\nsaved to %s" % out_file_name, file=orig_stdout, end='')


if __name__ == '__main__':
    main()
    #tests()
