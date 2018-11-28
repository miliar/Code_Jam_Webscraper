""" imports """
#pylint: disable=W0622
#pylint: disable=E0102
from __future__ import division
import glob, pickle, os, time, sys, argparse
from collections import OrderedDict
from copy import copy
from numpy import array, sin, cos
import numpy as np
from pylab import *
from pprint import pprint

""" global variables """

""" classes """

""" functions """
def solve(strings): #pylint: disable=W0621
    edits_count = 0
    prev_c = ''
    for c in copy(strings[0]):
        if c == prev_c:
            continue
        prev_c = c
        num_chars_per_str = []
        new_strings = []
        for string in strings:
            if not string or string[0] != c:
                return "Fegla Won"
            counter = 0
            while string and string[0] == c:
                string.pop(0)
                counter += 1
            assert counter > 0
            num_chars_per_str.append(counter)
            new_strings.append(string)
        strings = new_strings

        num_chars_solution = int(array(num_chars_per_str).mean())
        for num_chars in num_chars_per_str:
            edits_count += abs(num_chars - num_chars_solution)

    if sum([len(x) for x in strings]) == 0:
        return edits_count
    else:
        return "Fegla Won"


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
def read_floats():
    return [float(x) for x in read_line().split(' ')]
(numquestions,) = read_ints()
for questionindex in xrange(numquestions):
    ### parse input ###
    N, = read_ints()
    strings = [list(read_line()) for _ in range(N)]

    ### calculate answer ###
    answer = solve(strings)
    assert answer != None

    ### output ###
    #print "Calculating case #{}...".format(questionindex+1)
    answer_str = "Case #{}: {}".format(questionindex+1, answer)
    output += answer_str + '\n'
    print answer_str

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
            def filter_test_number(line):
                if line.startswith("Case #"):
                    parts = line.split('#')
                    parts[1] = parts[1][parts[1].index(':'):]
                    return '#'.join(parts)
                else:
                    return line
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

    except AssertionError as ex:
        print "\nFAILED:"
        print str(ex)
    print
