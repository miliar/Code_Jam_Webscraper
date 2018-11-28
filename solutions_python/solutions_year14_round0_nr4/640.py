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


def pk(naomi, ken, N):
    win_y = 0
    win_z = 0

    # rest of ken for y
    ken_y = ken[:]
    # rest of ken for z
    ken_z = ken[:]

    for i in range(N):
        ########
        # y ####
        ########
        # naomi lose
        if naomi[i] < ken_y[0]:
            ken_y = ken_y[:-1]
        # naomi win
        else:
            win_y += 1
            ken_y = ken_y[1:]

        ########
        # z ####
        ########
        # naomi win
        if naomi[i] > ken_z[-1]:
            win_z += 1
            ken_z = ken_z[1:]
        # naomi lose
        else:
            for j in range(len(ken_z)):
                if ken_z[j] > naomi[i]:
                    ken_z = ken_z[:j] + ken_z[j + 1:]
                    break

    return win_y, win_z


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
            N = int(infile.readline())
            naomi = sorted([float(item) for item in infile.readline().split()])
            ken   = sorted([float(item) for item in infile.readline().split()])
            (y, z) = pk(naomi, ken, N)
            outfile.write("Case #%d: %d %d\n" % (i, y, z))

    if None != args.outfile:
        outfile.close()

if __name__ == '__main__':
    main(getargs())
