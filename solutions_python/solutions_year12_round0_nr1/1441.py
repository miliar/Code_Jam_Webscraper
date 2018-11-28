#!/usr/bin/env python
import fileinput
import sys
import string

lines_per_case = 1

table = string.maketrans('ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvyeqz', 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upaozq')

def solve_case(case):
    return string.translate(case[0].strip(), table)


def produce_output(index, solution):
    print 'Case #{0}: {1}'.format(index, solution)


def get_test_cases(lines, n_of_lines_per_case=1):
    x = 0
    while x < len(lines):
        y = x + n_of_lines_per_case
        yield lines[x:y]
        x = y

if __name__ == "__main__":
    lines = []
    if(len(sys.argv) > 1):
        fn = sys.argv[1]
        with open(fn) as f:
            lines = f.readlines()
    else:
        for line in fileinput.input():
            lines.append(line)

    if len(lines) > 0:
        #nt = int(lines[0])
        for index, case in enumerate(get_test_cases(lines[1:], lines_per_case), 1):
            produce_output(index, str(solve_case(case)))
