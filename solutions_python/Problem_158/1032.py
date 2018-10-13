#!/usr/bin/env python

import numpy as np
import sys
import re


def solve(X, R, C):
    if X == 1:
        return 'GABRIEL'
    if X == 2:
        if R*C % 2:
            return 'RICHARD'
        else:
            return 'GABRIEL'
    if X == 3:
        if R*C in [6, 9, 12]:
            return 'GABRIEL'
        else:
            return 'RICHARD'
    if X == 4:
        if R*C in [12, 16]:
            return 'GABRIEL'
        else:
            return 'RICHARD'


def main():
    # check input arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        sys.stderr.write("Usage:\n")
        sys.stderr.write("\t%s input_file\n" % sys.argv[0])
        sys.exit(1)

    # check if input file name fits the model '{A,B,C}-{small,large}-{int}.in'
    output_file = None
    if re.search('[A,B,C]-(small|large)-(\d+).in', input_file) is not None:
        output_file = '%s.out' % input_file.split('.')[0]
        output_stream = open(output_file, 'w')
        sys.stdout = output_stream

    # open input file
    f = open(input_file)
    T = int(f.readline())
    sys.stderr.write("%d test cases\n" % T)

    for i in range(T):
        # read input data
        X, R, C = [int(x) for x in f.readline().split()]

        # call the function that solves the problem
        answer = solve(X, R, C)

        # print the answer
        print "Case #%d: %s" % (i+1, answer)

    # close output_stream
    if output_file is not None:
        sys.stdout = sys.__stdout__
        output_stream.close()


if __name__ == '__main__': main()
