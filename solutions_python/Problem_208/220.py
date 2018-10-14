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


####################################################################
#                           Solution                               #
####################################################################


def case(horses, distances):

    available_horses = [[0, 0, 0]]
    for i, (d, sp) in enumerate(horses[:-1]):
        best_time = min(t for d, sp, t in available_horses)
        available_horses.append([d, sp, best_time])

        next_d = distances[i][i+1]
        assert next_d > 0

        new_h = []
        for dd, spp, t in available_horses:
            if dd >= next_d:
                new_h.append([dd-next_d, spp, t+next_d/float(spp)])
        available_horses = new_h

    return min(t for d, sp, t in available_horses)





####################################################################
#                              I/O                                 #
####################################################################

def main():
    ################################################################
    # Define input and output
    #in_file_name = 'example.in'
    in_file_name = 'C-small-attempt0.in'
    #in_file_name = 'C-large.in'
    out_file_name = in_file_name.rstrip('.in') + '.out'
    # will be closed by garbage collector
    orig_stdout = sys.stdout
    sys.stdin = open(in_file_name)
    sys.stdout = open(out_file_name, "w")
    ################################################################

    for i in range(read_int()):
        n, q = read_ints()
        assert q == 1
        horses = []
        for _ in range(n):
            horses.append(read_ints())
        distances = []
        for _ in range(n):
            distances.append(read_ints())
        read_ints()
        solution = case(horses, distances)
        print(".", file=orig_stdout, end='')
        print("Case #%s: %s" % (i+1, solution))
    print("\nsaved to %s" % out_file_name, file=orig_stdout, end='')


if __name__ == '__main__':
    main()
    #tests()
