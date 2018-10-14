#!/usr/bin/env python

import numpy as np
import sys


def solve(A, B, K):
    out = 0
    for a in range(A):
        for b in range(B):
            if (a & b) < K:
                out += 1
    return out



def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        sys.stderr.write("Usage:\n")
        sys.stderr.write("\t%s input_file\n" % sys.argv[0])
        sys.exit(1)

    f = open(input_file)
    T = int(f.readline())
    sys.stderr.write("%d test cases\n" % T)

    for i in range(T):
        # read input data
        l = f.readline().split()
        A = int(l[0])
        B = int(l[1])
        K = int(l[2])
        #sys.stderr.write("%d %d %d\n" % (A, B, K))

        # call the function that solves the problem
        answer = solve(A, B, K)

        # print the answer
        print "Case #%d: %d" % (i+1, answer)


if __name__ == '__main__': main()


