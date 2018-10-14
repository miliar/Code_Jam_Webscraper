""" imports """
from __future__ import division
import glob, pickle, os, time, sys, argparse
from copy import copy
from numpy import array, sin, cos
import numpy as np
from pylab import *
from pprint import pprint

""" global variables """

""" classes """

""" functions """
def bounded(x, minval=0, maxval=float('inf')):
    return max(minval, min(maxval, x))

def is_possible(R, C, M, N):
    if N == 0:
        return True
    minrc = min(R, C)
    if N == 1:
        return True
    elif minrc == 1:
        return N > 1
    elif minrc == 2:
        return N > 3 and N%2 == 0
    else:
        return N > 3 and N not in [5, 7]

def do_checks(R, C, M, N, num_cols, num_rows, result):
    print result
    assert 0 <= num_cols <= C
    assert 0 <= num_rows <= R
    assert num_cols*num_rows >= N
    assert result.count('.') + result.count('c') == N, '{} empty spaces'.format(result.count('.') + result.count('c'))
    assert result.count('*') == M
    assert len(result.strip().split('\n')) == R

def solve(R, C, M):
    N = R*C - M
    num_cols = int(bounded(bounded(np.ceil(N/R), minval=2), maxval=C))
    if C > 2 and num_cols == 2 and N%2 == 1:
        num_cols = 3
    num_rows = int(bounded(bounded(np.ceil(N/num_cols))))
    if N == 9 and min(R,C) >= 3:
        num_cols = num_rows = 3
    print "R = {}, C = {}, M = {}, N = {}, num_cols = {}, num_rows = {}".format(R, C, M, N, num_cols, num_rows)

    assert 0 <= num_cols <= C
    assert 0 <= num_rows <= R
    assert num_cols*num_rows >= N

    if not is_possible(R, C, M, N):
        return "Impossible"

    if N == 1:
        def is_empty(r,c):
            return r==c==0
    else:
        def is_empty(r, c):
            if c >= num_cols:
                return False
            if r >= num_rows:
                return False
            last_col = c == num_cols - 1
            last_row = r == num_rows - 1
            if min(R, C) == 1:
                empty_box_flip = False
            else:
                empty_box_flip = N == (num_rows-1)*num_cols+1
            if last_col and last_row:
                return N == num_rows * num_cols
            elif last_col:
                if empty_box_flip:
                    return r < num_rows - 2
                else:
                    return True
            elif last_row:
                if c < 2:
                    return True
                else:
                    return c < (N - (num_rows-1)*num_cols)
            return True

    result = ""
    for r in range(R):
        for c in range(C):
            if r == c == 0 and N != 0:
                result += 'c'
            elif is_empty(r, c):
                result += '.'
            else:
                result += '*'
        result += "\n"

    do_checks(R, C, M, N, num_cols, num_rows, result)
    return result.strip()


""" parse input """
## parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("filename", default="default.in", nargs='?')
parser.add_argument("-t", "--test", action="store_true")
parser.add_argument("-l", "--lazytest", action="store_true")
args = parser.parse_args()
output = ""
TIC = time.time()

## read input lines
input_lines = open(args.filename).readlines()
def read_line():
    return input_lines.pop(0).strip()
def read_ints():
    return [int(x) for x in read_line().split(' ')]
(numquestions,) = read_ints()
for questionindex in xrange(numquestions):
    ### parse input ###
    R, C, M = read_ints()

    ### calculate answer ###
    answer = solve(R, C, M)

    ### output ###
    #print "Calculating case #{}...".format(questionindex+1)
    answer_str = "Case #{}:\n{}".format(questionindex+1, answer)
    output += answer_str + '\n'
    # print answer_str

## write output
ofile = open('output', 'w').write(output)
TOC = time.time()
#print "done in {} s".format(TOC-TIC)


""" test """
if args.test:
    def filter_extension(filename):
        filename_parts = filename.split('.')
        if len(filename_parts) > 1:
            filename_parts = filename_parts[:-1]
        return '.'.join(filename_parts)

    print
    print "== TESTING VALIDITY =="

    try:
        # check if all input was used
        assert not len([l for l in input_lines if l.strip()]), "Not all input was used"

        # filter extension of filename
        filename_without_extension = filter_extension(args.filename)

        # get calculated and correct lines
        calculated_lines = [l.strip() for l in output.split('\n') if l.strip()]
        correct_lines = [l.strip() for l in open("{}.out".format(filename_without_extension)).readlines() if l.strip()]

        # check if number of lines match
        assert len(correct_lines) == len(calculated_lines), "calculated {} lines but expected {}".format(len(calculated_lines), \
                                                            len(correct_lines))

        # apply lazytest: filter away test numer
        unfiltered_calculated_lines = calculated_lines
        unfiltered_correct_lines = correct_lines
        if args.lazytest:
            def filter_test_number(l):
                if l.startswith("Case #"):
                    parts = l.split('#')
                    parts[1] = parts[1][parts[1].index(':'):]
                    return '#'.join(parts)
                else:
                    return l
            calculated_lines = [filter_test_number(l) for l in calculated_lines]
            correct_lines = [filter_test_number(l) for l in correct_lines]

        # get lines that don't match
        incorrect_line_numbers = []
        for line_number, (correct_line, calculated_line) in enumerate(zip(correct_lines, calculated_lines)):
            if correct_line != calculated_line:
                incorrect_line_numbers.append(line_number)
        if len(incorrect_line_numbers):
            error_msg = "\n"
            for line_number in incorrect_line_numbers:
                error_msg += '    "{}"  should be  "{}"\n'.format(unfiltered_calculated_lines[line_number],
                                                                  unfiltered_correct_lines[line_number])
            raise AssertionError(error_msg)

        print "SUCCESS"

    except AssertionError as e:
        print "\nFAILED:"
        print str(e)
    print
