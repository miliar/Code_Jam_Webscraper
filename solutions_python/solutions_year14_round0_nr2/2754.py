#!/usr/bin/env python

from __future__ import print_function

import sys
from collections import defaultdict


def main(*args):
    if(len(args) < 2):
        print("Usage: %s <input file>" % args[0])

    filename = args[1]
    input_file = open(filename, "rb")
    output_file = open(filename+".out", "wb")

    try:
        in_str = input_file.readline().strip()
    except:
        print("Premature end of input")

    T = int(in_str)
    for k in range(T):
        input_strs = input_file.readline().split()
        C = float(input_strs[0])
        F = float(input_strs[1])
        X = float(input_strs[2])

        time_taken = 0.0
        cookie_rate = 2.0
        while(True):
            if(X/cookie_rate < (C/cookie_rate + X/(F+cookie_rate)) ):
                time_taken += X / cookie_rate
                # print('Time taken:', time_taken)
                # print('cookie_rate:', cookie_rate)
                break
            else:
                time_taken += C / cookie_rate
                cookie_rate += F
                # print('Time taken:', time_taken)
                # print('cookie_rate:', cookie_rate)

        print("Case #%d: %0.7f" % (k+1, time_taken), file=output_file)
        
    input_file.close()
    output_file.close()


if(__name__ == "__main__"):
    sys.exit(main(*sys.argv))

