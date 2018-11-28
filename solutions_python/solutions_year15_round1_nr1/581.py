#!/usr/bin/env python

import numpy as np
import sys
import re
import os
import multiprocessing


def diffx(l):
    out = []
    for k, x in enumerate(l[:-1]):
        out.append(x - l[k+1])
    return out

def solve(l):
    d = diffx(l)

    out1 = 0
    for x in d:
        if x > 0:
            out1 += x

    out2 = 0
    m = max(d)
    for x in l[:-1]:
        out2 += min(x, m)
    return (out1, out2)


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
    if re.search('[A,B,C,D,E]-(small|large)-(attempt\d+).in', input_file) is not None:
        output_file = '%s.out' % input_file.split('.')[0]
        output_stream = open(output_file, 'w')
        sys.stdout = output_stream

    # open input file
    f = open(input_file)
    T = int(f.readline())
    sys.stderr.write("%d test cases\n" % T)

    for i in range(1, T+1):
        # read input data
        f.readline()
        l = [int(x) for x in f.readline().split()]

        # call the function that solves the problem
        sys.stderr.write("%d\n" % i)
        ans = solve(l)
        print "Case #%d: %d %d" % (i, ans[0], ans[1])

    # close output_stream
    if output_file is not None:
        sys.stdout = sys.__stdout__
        output_stream.close()


if __name__ == '__main__': main()
