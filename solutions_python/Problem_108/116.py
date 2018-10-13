#!/usr/bin/env python
import fileinput
import sys

lines_per_case = 2


def solve_case(case):
    n = int(case[0].strip())
    vines = dict(map(int, line.strip().split()) for line in case[1:-1])
    ledge = int(case[-1].strip())

    current_vine = int(case[1].strip().split()[0])

    if get_to_ledge(current_vine, current_vine, vines, ledge):
        return 'YES'
    return 'NO'


def get_to_ledge(vine, length, vines, ledge):
    max_ = vine + length
    if max_ >= ledge:
        return True
    for poss_v in xrange(max_, vine, -1):
        if poss_v in vines and get_to_ledge(poss_v, min(poss_v - vine, vines[poss_v]), vines, ledge):
            return True
    return False


def produce_output(index, solution):
    print 'Case #{0}: {1}'.format(index, solution)


def get_test_cases(lines, n_of_lines_per_case=1):
    x = 0
    while x < len(lines):
        n_of_lines_per_case = int(lines[x].strip()) + 2
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
