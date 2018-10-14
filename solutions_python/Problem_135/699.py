#!/usr/bin/env python
# coding: utf-8

#########################################################################
#########################################################################

"""
   File Name: A.py
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

    return parser.parse_args()


def main(args):
    """ Main entry.
    """

    with open(args.infile) as infile:
        T = int(infile.readline())
        for i in range(1, T + 1):
            rid1 = int(infile.readline())
            for j in range(rid1):
                line = infile.readline()
            ids1 = set([int(idx) for idx in line.split()])
            for j in range(rid1, 4):
                infile.readline()

            rid2 = int(infile.readline())
            for j in range(rid2):
                line = infile.readline()
            ids2 = set([int(idx) for idx in line.split()])
            for j in range(rid2, 4):
                infile.readline()

            pred = list(ids1.intersection(ids2))

            if len(pred) < 1:
                print "Case #%d: Volunteer cheated!" % (i, )
            elif len(pred) > 1:
                print "Case #%d: Bad magician!" % (i, )
            else:
                print "Case #%d: %d" % (i, pred[0])


if __name__ == '__main__':
    main(getargs())
