#!/usr/bin/python

import itertools
import argparse
import math
import pickle
import sys

digits="0123456789"

def palindromes(num_digits):
    """Returns a list of palindromes with num_digits digits.
    >>> palindromes(3)
    ['101', '202', '303', '404', '505', '606', '707', '808', '909', '111', '212', '313', '414', '515', '616', '717', '818', '919', '121', '222', '323', '424', '525', '626', '727', '828', '929', '131', '232', '333', '434', '535', '636', '737', '838', '939', '141', '242', '343', '444', '545', '646', '747', '848', '949', '151', '252', '353', '454', '555', '656', '757', '858', '959', '161', '262', '363', '464', '565', '666', '767', '868', '969', '171', '272', '373', '474', '575', '676', '777', '878', '979', '181', '282', '383', '484', '585', '686', '787', '888', '989', '191', '292', '393', '494', '595', '696', '797', '898', '999']
    >>> palindromes(2)
    ['11', '22', '33', '44', '55', '66', '77', '88', '99']
    >>> palindromes(1)
    ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    """
    
    if num_digits==1:
        return list(digits[1:])
    l=list(itertools.product(digits, repeat=num_digits/2))
    l=[''.join(i) for i in l if i[0]!="0"]
    
    # Even number of digits
    if num_digits%2==0:     
        result=[i+i[::-1] for i in l]
    # Odd number of digits
    else:
        result=[]
        for d in digits:
            result+=[i+d+i[::-1] for i in l]
    return result


def palindromes_digit_range(max_digits):
    result=[palindromes(num_digits) for num_digits in range(1, max_digits+1)]
    return [long(item) for sublist in result for item in sublist]

def root_list(l):
    l=set(l)
    return [i for i in l if math.sqrt(i) in l]

def parse_google_input(list_of_fair_and_squares):
    lines=sys.stdin.readlines()
    for i in range(1, len(lines)):
        line = lines[i]
        min_num, max_num = [int(n) for n in line.split()]
        print "Case #%d: %d" % (i, len([n for n in list_of_fair_and_squares if min_num <= n <= max_num]))

################################ Unit test mode ################################

FILENAME="fair_and_square_numbers"

parser = argparse.ArgumentParser(description='Solve Google code jam qualification round, question 2.')
parser.add_argument('-t', '--test', action='store_true',
                    help="Test mode: run unit tests and exit")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-p', '--prepare', metavar="MAX_DIGITS",
                   type=int, help="Prepare list of fair and square numbers in offline mode")
group.add_argument('-c', '--check',  action="store_true",
                   help="Check input with pre-computed list of numbers")

args = parser.parse_args()
if args.test:
    import doctest
    doctest.testmod(verbose=True)
elif args.check:
    list_of_fair_and_squares=pickle.load(open(FILENAME))
    parse_google_input(list_of_fair_and_squares)
    
else:
    l=palindromes_digit_range(args.prepare)
    fair_and_squares = root_list(l)
    pickle.dump(fair_and_squares , open(FILENAME , "wb" ) )
    print fair_and_squares

