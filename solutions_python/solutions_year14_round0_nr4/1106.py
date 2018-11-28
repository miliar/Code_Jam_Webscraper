#!/usr/bin/python3

import re
#import matplotlib.pyplot as plt
import sys
import itertools
import math
import logging
from functools import partial
import argparse

# CodeJam I/O helpers adapted from royf

# A single word (minus whitespace)
def read_word(f):
    return next(f).strip()

# A single int (given base)
def read_int(f, base=10):
    return int(read_word(f), base)

# A single float
def read_float(f):
    return float(read_word(f))

# A list of characters (including whitespace)
def read_letters(f):
    return list(read_word(f))

# A list of digits (whitespace results in error)
def read_digits(f, base=10):
    return [int(x, base) for x in read_letters(f)]

# A list of words split by whitespace
def read_words(f, delimiter=' '):
    return read_word(f).split(delimiter)

# A list of values interpreted by converter, split by delimiter
def read_values(f, converter, delimiter=' '):
    return [converter(x) for x in read_words(f, delimiter)]

# A list of ints split by whitespace
def read_ints(f, base=10, delimiter=' '):
    return read_values(f, partial(int,base=base), delimiter)

# Read 'length' lines, return a list interpreting each line using 'reader=read_ints'
# Use functools.partial to specify reader arguments
def read_arr(f, length, reader=read_ints):
    res = []
    for _i in range(length):
        res.append(reader(f))
    return res

def IsApproximatelyEqual(x, y, epsilon):
    """Returns True iff y is within relative or absolute 'epsilon' of x.

    By default, 'epsilon' is 1e-6.
    """
    # Check absolute precision.
    if -epsilon <= x - y <= epsilon:
        return True

    # Is x or y too close to zero?
    if -epsilon <= x <= epsilon or -epsilon <= y <= epsilon:
        return False

    # Check relative precision.
    return (-epsilon <= (x - y) / x <= epsilon
             or -epsilon <= (x - y) / y <= epsilon)

def solve(in_file, out_fn=None):
    if out_fn is None:
        out_fn = re.match('(.+)\.in',in_file.name).groups()[0] + '.out'
    with open(out_fn, 'w') as fo:
        setup()
        T = read_int(in_file)
        for case_num in range(1, T+1):
            case = read_case(in_file)
            answer = solver(case)
            logging.info("Solved case {}".format(case_num))
            write_case(fo, case_num, answer)

################################################################################

def read_case(f):
    blocks = read_int(f)
    n = read_values(f, float)
    k = read_values(f, float)
    return (n,k)

def write_case(f, case_num, answer):
    output = "Case #{}: {}\n".format(case_num, answer) 
    logging.debug(output)
    f.write(output)

################################################################################

def write_tests(outfilename, size, numcases=None):
    import random

    small = size == 'small'

    if numcases == None:
        if small:
            numcases = 50
        else:
            numcases = 50

    if small:
        bmax=10
    else:
        bmax=1000

    cases = []
    for tnum in range(numcases):
        blocks = random.randint(1,bmax)
        n = ["{:.5}".format(random.random()) for _ in range(blocks)]
        k = ["{:.5}".format(random.random()) for _ in range(blocks)]

        case = "{}\n{}\n{}\n".format(blocks," ".join(n)," ".join(k))

        cases.append(case)

    with open(outfilename,'w') as outfile:
        outfile.write("{}\n".format(numcases))
        for case in cases:
            outfile.write(case)
        outfile.close()

################################################################################

def solver(case):
    logging.debug(case)
    n,k=case
    n = sorted(n)
    k = sorted(k)

    def war(n,k):
        #logging.debug("War: {} {}".format(n,k))
        points = 0
        for b in n:
            # keith plays smallest that beats n, or smallest overall
            for pos,kb in enumerate(k):
                if kb>b:
                    del k[pos]
                    break
            else:
                del k[0]
                points += 1

        return points

    def deceitful_war(n,k):
        score = 0 
        while len(n) > 0:
            logging.debug("Deceitful War:\n{}\n{}".format(n,k))
            if (n[0] < k[0]):
                # play ones that are smaller than all of keith's in exchange for keith's biggest
                del n[0]
                del k[-1]
            else:
                # else my smallest is bigger than keith's smallest; say it is very large and get both smallest ones to be played
                del n[0]
                del k[0]
                score += 1
        return score


    return "{} {}".format(deceitful_war(n.copy(),k.copy()),war(n.copy(),k.copy()))

# Globals
def setup():
    return

################################################################################

parser = argparse.ArgumentParser()
parser.add_argument('testfile', nargs='?', type=argparse.FileType('r'), help='Name of file to solve (must end with ".in")')
parser.add_argument( '--tests',  nargs='?', const="tests.in", help='Write tests instead of solving them')
parser.add_argument('--testsize', choices=["small","large"], metavar="SIZE", default="small", help="whether to make large or small tests")
parser.add_argument('--testcases', type=int, metavar="N", help="Number of test cases to produce")
args = parser.parse_args()

logging.basicConfig(format="%(message)s", level=logging.INFO)
if args.tests:
    write_tests(args.tests, args.testsize, args.testcases)
else:
    if args.testfile:
        solve(args.testfile)
    else:
        parser.error("You must specify an input filename if not using --tests")
