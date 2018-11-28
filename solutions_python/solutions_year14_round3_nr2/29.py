""" imports """
#pylint: disable=W0622
#pylint: disable=E0102
#pylint: disable=W0621
from __future__ import division
import glob, pickle, os, time, sys, argparse
from copy import copy
from numpy import array, sin, cos
import numpy as np
from pylab import *
from pprint import pprint
from itertools import permutations
from math import factorial

""" global variables """

""" classes """

""" functions """
def valid_perm(perm):
    used_chars = set()
    last_char = ''
    for car in perm:
        for c in car:
            if c != last_char:
                if c in used_chars:
                    return False
            last_char = c
            used_chars.add(c)
    return True

def simplify(cars):
    newcars = []
    for car in cars:
        newcar = ""
        prev_c = ''
        for c in car:
            if c != prev_c:
                newcar += c
                prev_c = c
        if len(newcar) != len(set(newcar)):
            return ["bab"]
        newcars.append(newcar)
    return newcars

def simplify_doubles(cars, possibilities_factor):
    prev_car = ''
    prev_car_count = 1
    for car in sorted(cars):
        if car == prev_car:
            prev_car_count += 1
            possibilities_factor *= prev_car_count
            cars.remove(car)
            if len(car) > 1:
                return ["bab"], 1
        else:
            prev_car_count = 1
        prev_car = car
    return cars, possibilities_factor

def split_independents(cars):
    remaining = set(cars)
    independents = []
    while remaining:
        car = remaining.pop()
        used_chars = set(car)
        prev_used_chars = set()
        similar_cars = [car]
        while len(prev_used_chars) != len(used_chars):
            prev_used_chars = set(used_chars)
            for other_car in set(remaining):
                for c in other_car:
                    if c in used_chars:
                        similar_cars.append(other_car)
                        remaining.remove(other_car)
                        for c in other_car:
                            used_chars.add(c)
                        break
                if len(prev_used_chars) != len(used_chars):
                    break


        independents.append(similar_cars)
    assert sum(len(x) for x in independents) == len(cars), [independents, cars]
    return independents

def remove_singles(cars):
    return [car for car in cars if len(car) > 1]

def is_possible(cars):
    if not cars:
        return True

    def car_is_possible(car):
        return len(set(car)) == len(car)
    for car in cars:
        if not car_is_possible(car):
            return False

    remaining = set(cars)
    first_car = last_car = remaining.pop()
    used_chars = set(last_car)
    while remaining:
        for other_car in remaining:
            if last_car[-1] == other_car[0]:
                last_car = other_car
                remaining.remove(last_car)
                for c in last_car[1:]:
                    if c in used_chars:
                        return False
                    used_chars.add(c)
                break
            if first_car[0] == other_car[-1]:
                first_car = other_car
                remaining.remove(first_car)
                for c in first_car[:-1]:
                    if c in used_chars:
                        return False
                    used_chars.add(c)
                break
        else:
            return False
    return True

def solve(cars):
    possibilities_factor = 1

    cars = simplify(cars)
    cars, possibilities_factor = simplify_doubles(cars, possibilities_factor)

    independents = split_independents(cars)
    independents = [remove_singles(case) for case in independents]
    print cars, independents

    for case in independents:
        # counter = 0
        # for perm in permutations(case):
        #     if valid_perm(perm):
        #         counter += 1
        # possibilities_factor *= counter
        # assert counter == 1 or counter == 0

        # print case, is_possible(case)
        # assert (counter == 1) == is_possible(case)

        if not is_possible(case):
            return 0
    return possibilities_factor * factorial(len(independents)) % 1000000007


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
    cars = [c for c in read_line().split(' ')]
    assert len(cars) == N, cars

    ### calculate answer ###
    answer = solve(cars)
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
