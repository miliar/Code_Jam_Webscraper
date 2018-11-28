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
import copy


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


X = 0
Y = 0


def get_idx(s):
    idx_set = set()
    for i in range(len(s)):
        idx_set.add(s[:i+1])
    return idx_set


def allcase(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret


def calc(N, S, v_servers, curX):
    global X, Y

    empties = [i for i in range(N) if len(v_servers[i]) == 0]

    if len(S) == len(empties):
        curX += sum(len(s) for s in S)
        if curX > X:
            Y = allcase(len(S))
            X = curX
        elif curX == X:
            Y += allcase(len(S))
    elif len(S) > 0:
        s = S[0]
        for i in range(N):
            v_servers_copy = copy.deepcopy(v_servers)
            v_servers_copy[i] = v_servers_copy[i].union(s)
            curInc = len(v_servers_copy[i]) - len(v_servers[i])
            calc(N, S[1:], v_servers_copy, curX+curInc)
    else:
        if curX > X:
            Y = 1
            X = curX
        elif curX == X:
            Y += 1


def solve(M, N, S):
    global X, Y
    calc(N, [get_idx(s) for s in S], [set() for i in range(N)], 0)
    return "%d %d" % (X + N, Y)


def main(args):
    """ Main entry.
    """

    global X, Y

    if None == args.outfile:
        outfile = sys.stdout
    else:
        outfile = open(args.outfile, "w")

    with open(args.infile) as infile:
        T = int(infile.readline())
        for i in range(1, T + 1):
            [M, N] = [int(item) for item in infile.readline().split()]
            S = [infile.readline().strip() for j in range(M)]
            outfile.write("Case #%d: %s\n" % (i, solve(M, N, S)))
            X = 0
            Y = 0

    if None != args.outfile:
        outfile.close()

if __name__ == '__main__':
    main(getargs())
