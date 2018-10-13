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

def case(n):
    digits = [int(d) for d in str(n)]
    first_i_with_value = 0
    for i in range(len(digits)-1):
        if digits[i] < digits[i+1]:
            first_i_with_value = i+1
        if digits[i] > digits[i+1]:
            digits[first_i_with_value] -= 1
            for j in range(first_i_with_value+1, len(digits)):
                digits[j] = 9
            break
    return int(''.join(str(d) for d in digits))



####################################################################
#                              I/O                                 #
####################################################################

def main():
    ################################################################
    # Define input and output
    #in_file_name = 'example.in'
    #in_file_name = 'B-small-attempt0.in'
    in_file_name = 'B-large.in'
    out_file_name = in_file_name.rstrip('.in') + '.out'
    # will be closed by garbage collector
    orig_stdout = sys.stdout
    sys.stdin = open(in_file_name)
    sys.stdout = open(out_file_name, "w")
    ################################################################

    for i in range(read_int()):
        solution = case(read_int())
        print(".", file=orig_stdout, end='')
        print("Case #%s: %s" % (i+1, solution))
    print("\nsaved to %s" % out_file_name, file=orig_stdout, end='')


if __name__ == '__main__':
    main()
