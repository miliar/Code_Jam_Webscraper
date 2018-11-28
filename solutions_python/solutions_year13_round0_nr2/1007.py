#!/usr/bin/env python2
# by Santiago Saavedra

from multiprocessing import Pool, Queue

from collections import deque
from itertools import repeat

flat = lambda l: [item for sublist in l for item in sublist]

def parse_case(case):
    if len(case) != len(case[0]):
        if len(case) > len(case[0]):
            case = zip(*case[::-1])
        for i in range(len(case[0]) - len(case)):
            case.append(list(repeat(0, len(case[0]))))
    flat_case = flat(case)
    initial = max(flat_case)
    last = min(flat_case)

    valid_states = deque([ case ])

    def is_line_valid(level, line):
        if level in line and max(line) > level:
            return line
            return map(lambda x: False if x > level else x, line)
        return map(lambda x: True if x == level else x, line)

    for current in range(last, initial + 1)[::-1]:
        for state in valid_states:
            a = map(lambda line: is_line_valid(current, line), state)
            b = map(lambda line: is_line_valid(current, line), map(list, zip(*state)[::-1]))
            bz = zip(*b[::-1])
            bz = zip(a, bz)
            
            for lines in bz:
                ok = False
                for line in lines:
                    if max(line) <= current:
                        ok = True
                        break
                    if all(map(lambda x: (type(x) is bool and x) or x != current, line)):
                        ok = True
                        break
                if not ok:
                    return 'NO'
    return 'YES'
    pass

def parse_input(lines):
    num = int(lines[0])
    cases = []
    l = 1
    for i in range(num):
        m, n = map(int, lines[l].split())
        l += 1
        case = map(lambda x: map(int, x.split()), lines[l:l+m])
        l += m
        cases.append(case)

    return cases

def main():
    import sys
    cases = parse_input(map(lambda a: a.replace("\n", ''), sys.stdin.readlines()))

    # rcases = [ parse_case(cases[2]) ]
    rcases = map(parse_case, cases)
   
    for i, case in enumerate(rcases, start=1):
        print "Case #%d: %s" % (i, case)

if __name__ == '__main__':
    main()




