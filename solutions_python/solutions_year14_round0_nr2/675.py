#!/usr/bin/env python
# coding: utf-8

#########################################################################
#########################################################################

"""
   File Name: gcj.py
      Author: Wan Ji
      E-mail: wanji@live.com
  Created on: Sat Apr 12 14:59:24 2014 CST
"""
DESCRIPTION = """
"""

import os
import sys
import argparse


def perr(msg):
    """ Print error message.
    """

    sys.stderr.write("%s" % msg)
    sys.stderr.flush()


def pinfo(msg):
    """ Print information message.
    """

    sys.stdout.write("%s" % msg)
    sys.stdout.flush()


def runcmd(cmd):
    """ Run command.
    """

    perr("%s\n" % cmd)
    os.system(cmd)


def getargs():
    """ Parse program arguments.
    """

    parser = argparse.ArgumentParser(description=DESCRIPTION,
                                     formatter_class=
                                     argparse.RawTextHelpFormatter)
    parser.add_argument('infile', type=str, help='input file')
    parser.add_argument('outfile', type=str, nargs='?', default=None,
                        help='output file')

    return parser.parse_args()


def least_secs(C, F, X):
    # rest of X
    rest = X
    # past secs
    past = 0
    # inc. speed
    speed = 2

    while True:
        # rest time for getting C cookies
        time4C = C / speed
        # rest time for getting X cookies
        time4X = rest / speed
        if time4X <= time4C:
            return past + time4X
        speed += F
        new_time4X = time4C + rest / speed
        if time4X <= new_time4X:
            return past + time4X
        past += time4C
        #past += new_time4X
        #rest -= new_time4X * speed

    return 0


def main(args):
    """ Main entry.
    """

    if None == args.outfile:
        outfile = sys.stdout
    else:
        outfile = open(args.outfile, "w")

    with open(args.infile) as infile:
        T = int(infile.readline())
        for i in range(1, T + 1):
            [C, F, X] = [float(item) for item in infile.readline().split()]
            outfile.write("Case #%d: %.7f\n" % (i, least_secs(C, F, X)))

    if None != args.outfile:
        outfile.close()

if __name__ == '__main__':
    main(getargs())
