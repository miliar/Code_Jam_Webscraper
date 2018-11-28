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

def test_case(s, k):
    pancakes = (c == '+' for c in s)
    moves = 0
    flipped = False
    flip_changes = [False] * len(s)
    for i, origP in enumerate(pancakes):
        flipped ^= flip_changes[i]
        newP = origP ^ flipped

        if not newP:
            if i + k > len(s):
                return 'IMPOSSIBLE'
            else:
                moves += 1
                flipped ^= True
                if i + k < len(s):
                    flip_changes[i+k] = True

    return moves


####################################################################
#                              I/O                                 #
####################################################################

def main():
    ################################################################
    # Define input and output
    #in_file_name = 'example.in'
    #in_file_name = 'A-small-attempt0.in'
    in_file_name = 'A-large.in'
    out_file_name = in_file_name.rstrip('.in') + '.out'
    # will be closed by garbage collector
    orig_stdout = sys.stdout
    sys.stdin = open(in_file_name)
    sys.stdout = open(out_file_name, "w")
    ################################################################

    for i in range(read_int()):
        s, k = input().split()
        k = int(k)
        solution = test_case(s, k)
        print(".", file=orig_stdout, end='')
        print("Case #%s: %s" % (i+1, solution))
    print("\nsaved to %s" % out_file_name, file=orig_stdout, end='')


if __name__ == '__main__':
    main()
