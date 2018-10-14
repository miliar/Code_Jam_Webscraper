#!/usr/bin/env pypy

import sys

# file_name = 'Sample.in'
# file_name = 'B-small-attempt0.in'
# file_name = 'A-small-attempt0.in'
file_name = 'B-large.in'

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
cas = None
n = None
for lin in in_lines:
    if n is None:
        n = int(lin.split()[0])
        cas = []
        continue
    if n == 0:
        n = int(lin.split()[0])
        tests.append(tuple(cas))
        cas = []
        continue
    else:
        n -= 1
        row = [int(i) for i in lin.split()]
        cas.append(tuple(row))
tests.append(tuple(cas))
tests = tuple(tests)
# from pprint import pprint
# pprint(tests)


def result(cas):
    num_row = len(cas)
    num_col = len(cas[0])

    row_max = []
    for i in range(num_row):
        row_max.append(max(cas[i]))
    row_max = tuple(row_max)
    # print row_max

    col_max = []
    for i in range(num_col):
        col_max.append(max([cas[j][i] for j in range(num_row)]))
    col_max = tuple(col_max)
    # print col_max

    for r in range(num_row):
        for c in range(num_col):
            e = cas[r][c]
            if e < row_max[r] and e < col_max[c]:
                return False
    return True

out_lines = []
for i in range(num_cases):
    lin = 'Case #' + str(i + 1) + ': '
    if result(tests[i]):
        lin += 'YES'
    else:
        lin += 'NO'
    out_lines.append(lin)
    print lin
# from pprint import pprint
# pprint(out_lines)

# test sample output
if 'Sample.in' == file_name:
    assert str(out_lines) == str(sample_out_lines)
