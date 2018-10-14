# -*- coding: utf-8 -*-

import sys
import itertools

class Robot(object):
    def __init__(self, seq):
        self.current_pos = 1
        self.seq = seq

    def need_steps(self):
        if self.seq:
            return abs(self.seq[0] - self.current_pos)
        return 0

    def push(self):
        steps = self.need_steps()
        self.current_pos = self.seq[0]
        self.seq = self.seq[1:]
        return steps + 1

    def move(self, steps):
        if self.seq:
            if self.current_pos != self.seq[0]:
                steps = min(steps, self.need_steps())
                if self.seq[0] > self.current_pos:
                    self.current_pos += steps
                else:
                    self.current_pos -= steps

def next(robots, seq):
    robot_idx = seq[0]
    steps = robots[robot_idx].push()
    robots[1-robot_idx].move(steps)
    return steps

def grouper(lst):
    args = [iter(lst)] * 2
    return itertools.izip_longest(*args)

def solve_case(case, limit):
    case = case.strip().split()
    case = map(lambda x: 1 if x == 'B' else 0 if x == 'O' else x, case)
    case = map(int, case)

    n = case[0]
    case = case[1:]
    seq = [i for i in grouper(case)]
    seq = seq[:limit]

    robots = [Robot([pos for idx, pos in seq if idx == 0]),
                Robot([pos for idx, pos in seq if idx == 1])]

    seq = [idx for idx, pos in seq]
    result = 0
    while seq:
        result += next(robots, seq)
        seq = seq[1:]
    return result

if __name__ == '__main__':
    if len(sys.argv) == 3:
        tp = sys.argv[2]
        f = open(sys.argv[1])
        if f:
            lst = []
            n = f.readline()
            idx = 1
            for l in f:
                limit = 100
                if tp == 'small':
                    limit = 10

                r = solve_case(l, limit)
                lst.append("Case #%s: %s\n" % (idx, r))

                if tp == 'small':
                    if idx > 20:
                        break
                elif tp == 'large':
                    if idx > 100:
                        break
                else:
                    print 'Invalid type'

                idx += 1

            out = open("output", "w")
            out.writelines(lst)
        else:
            print 'fail open'
    else:
        print 'error'
