#!/usr/bin/env python

import sys

class Horse:
    def __init__(self,initial_pos, max_speed):
        self.initial_pos = initial_pos
        self.max_speed = max_speed

class Case:
    def __init__(self,case_num, dest, horses=[]):
        self.case_num = case_num
        self.dest = dest
        self.horses = horses

    def add_horse(h):
        self.horses.append(h)


def handle_case(case):
    times = [(case.dest - h.initial_pos)/h.max_speed for h in case.horses]
    max_time = max(times)
    speed = case.dest / max_time
    return speed


with open(sys.argv[1], 'r') as my_file:
    first  = True
    num_lines = 0
    count = 1
    lines = []
    for line in my_file:
        if first:
            first = False
            continue
        else:
            lines.append(line.strip())

    cases = []
    while len(lines):
        [dest, num_horses] = lines[0].split(' ')
        def make_horse(line):
            [initial_pos, max_speed] = line.split(' ')
            return Horse(float(initial_pos), float(max_speed))
        next_case = Case(count, float(dest), map(make_horse, lines[1:1 + int(num_horses)]))
        lines = lines[int(num_horses) + 1:]
        cases.append(next_case)
        print('Case #%d: %s' % (count, str(handle_case(next_case))))
        count+=1
