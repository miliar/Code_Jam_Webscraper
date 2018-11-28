#!/bin/env python
import sys
import os
import argparse
import logging
import subprocess
import operator
from math import log, exp
_folder_path = os.path.split(os.path.abspath(__file__))[0]
sys.path.append(_folder_path)

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('infilename')
    parser.add_argument('outfilename')
    args = parser.parse_args()


    with open(args.infilename, "r") as inf:
        data = map(lambda x: x.split(), inf.readlines())

    T = int(data[0][0])
    data = data[1:] # skip T line

    print "len(data):", len(data)
    print "T:", T

    with open(args.outfilename, "w") as outf:
        for case in range(T):
            print "----------------"
            stats_line = data[2*case]
            prob_line = data[2*case+1]

            A = int(stats_line[0])
            B = int(stats_line[1])



            probs = [-float("inf") if (float(p))==0 else log(float(p)) for p in prob_line]
            running_sums = [None for i in range(A+1)]
            for n in range(A,-1,-1):
                if n==A:
                    running_sums[n] = 0
                else:
                    running_sums[n] = running_sums[n+1] + probs[A-n-1]

            e_enter = B + 2
            min_e = e_enter

            for n in range(0,A):
                e_backtrack_n = n + n + (B - A) + 1 + (1-exp(running_sums[n]))*(B+1)
                min_e = min(min_e, e_backtrack_n)


            print >>outf, "Case #%s: %s" % (case+1, min_e)
            print "----------------"











if __name__ == '__main__':
    main()

