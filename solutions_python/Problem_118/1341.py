#!/usr/bin/env pypy

import sys

#file_name = 'Sample.in'
# file_name = 'C-small-attempt0.in'
#file_name = 'B-small-attempt0.in'
file_name = 'C-small-attempt1.in'
# file_name = 'B-large.in'

# open input file
try:
    with open(file_name, 'r') as f:
        num_cases = int(f.readline())
        in_lines = [i.strip('\n') for i in f.readlines()]
except EnvironmentError:
    print "Can't open input file!"
    sys.exit(-1)
# from pprint import pprint
# print num_cases
# pprint(in_lines)

if 'Sample.in' == file_name:
    try:
        with open('Sample.out', 'r') as f:
            sample_out_lines = [i.strip('\n') for i in f.readlines()]
    except:
        print "Can't open sample output file"
        sys.exit(-2)
    # need to test smaple output later

# process the input file
tests = []
for lin in in_lines:
    cas = map(int, lin.split())
    tests.append(tuple(cas))
tests = tuple(tests)
#from pprint import pprint
#pprint(tests)


def is_pal(x):
    s = str(x)
    return s == s[::-1]

from math import sqrt


def is_fair_sqr(x):
    if not is_pal(x):
        return False

    r = int(sqrt(x))
    if r ** 2 == x and is_pal(r):
        # print x, r
        return True
    else:
        return False


def compute(cas):
    a, b = cas
    num = 0
    for i in range(a, b + 1):
        if is_fair_sqr(i):
            num += 1
    return num

# compute([3, 5])
# sys.exit()

out_lines = []
for i in range(num_cases):
    lin = 'Case #' + str(i + 1) + ': '
    lin += str(compute(tests[i]))
    out_lines.append(lin)
    print lin
# from pprint import pprint
# pprint(out_lines)

# test sample output
if 'Sample.in' == file_name:
    assert str(out_lines) == str(sample_out_lines)
