#!/usr/bin/python2.7

import sys

def read_config(f):
    row = int(f.readline())
    lines = [f.readline() for i in range(4)]
    return {int(v) for v in  lines[row - 1].split(' ')}

def solve_case(f):
    config1 = read_config(f)
    config2 = read_config(f)
    options = config1 & config2
    l = len(options)
    if l == 1:
        return str(list(options)[0])
    elif l == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'


def main(filename):
    with open(filename) as f:
        cases_count = int(f.readline())
        for case_num in range(cases_count):
            print 'Case #{}: {}'.format(case_num + 1, solve_case(f))

if __name__ == "__main__":
    main(sys.argv[1])
