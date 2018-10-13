#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

import sys

MIN_DEFAULT = 10**6 + 1

def split_candy(candies):
    minimum = MIN_DEFAULT
    total = 0
    check = 0
    for candy in candies:
        if candy < minimum:
            minimum = candy
        total += candy
        check ^= candy

    if check != 0:
        return 'NO'
    else:
        return total - minimum

def main(argv=None):
    if argv == None:
        argv = sys.argv

    if len(argv) <= 1:
        print('pass the input file name!')
        sys.exit(-1)

    input_file = open(argv[1], 'r')

    T = int(input_file.readline())
    for num_case in range(1, T + 1):
        num_candies = int(input_file.readline())
        candies = (int(c) for c in input_file.readline().split()[:num_candies])
        print('Case #{0}: {1}'.format(num_case, split_candy(candies)))

if __name__ == '__main__':
    main()
