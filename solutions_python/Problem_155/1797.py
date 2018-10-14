#!/usr/bin/env python

import numpy as np
import sys
import re


def solve(l):

    # compute partial sums
    s = [l[0]]
    for x in l[1:]:
        s.append(x + s[-1])

    # compute the minimal number of extra guests needed
    out = 0
    for i in range(1, len(l)):
        x = i - s[i-1]
        if x > 0:
            out += x
            for j in range(i, len(l)):
                s[j] += x

    return out 


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
        l = [int(x) for x in list(f.readline().split()[1])]

        # call the function that solves the problem
        answer = solve(l)

        # print the answer
        print "Case #%d: %s" % (i+1, answer)

    # close output_stream
    if output_file is not None:
        sys.stdout = sys.__stdout__
        output_stream.close()


if __name__ == '__main__': main()
