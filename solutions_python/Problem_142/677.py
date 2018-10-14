#!/usr/bin/python3

import sys
import math

class Case(object):
    def __init__(self, case_id):
        self.case_id = case_id

    def solve_case(self):
        self.convert_rep()

        self.is_poss = self.is_possible()
        if not self.is_poss:
            return

        l2 = []
        for i in range(len(self.short_str)):
            nbs = []
            for l in self.lines:
                nbs.append(l[i][1])

            l2.append(nbs)

        nb_moves = 0
        for e in l2:
            avg = sum([float(c) for c in e]) / len(e)
            target = round(avg)
            dist = sum([abs(target - a) for a in e])
            nb_moves += dist
        self.nb_moves = nb_moves
        

    def is_possible(self):
        s = [''.join([c[0] for c in l]) for l in self.lines]
        self.short_str = s[0]
        return len(set(s)) <= 1

    def __str__(self):
        return str(self.lines)

    def read_case(self, f):
        self.nb_strings = int(f.readline())
        self.lines = [f.readline().strip('\n') for x in range(self.nb_strings)]

    def convert_rep(self):
        for i in range(len(self.lines)):
            l = self.lines[i]

            new_rep = []

            cur_char = None
            length = 0
            for c in l:
                if c == cur_char:
                    length += 1
                else:
                    if length != 0:
                        new_rep.append((cur_char, length))
                    cur_char = c
                    length = 1

            if length != 0:
                new_rep.append((cur_char, length))

            self.lines[i] = new_rep

    def print_solution(self, o):
        print('Case #%d: ' % (self.case_id), file=o, end='')
        if not self.is_poss:
            print('Fegla won', file=o)
        else:
            print(self.nb_moves, file=o)

def main():
    (f, o) = open_files()

    nb = int(f.readline().strip())
    for case_id in range(1, nb + 1):
        case = Case(case_id)
        case.read_case(f)
        case.solve_case()
        case.print_solution(o)

def open_files():
    f = sys.stdin
    o = sys.stdout

    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')

    if len(sys.argv) == 3:
        f = open(sys.argv[1], 'r')
        o = open(sys.argv[2], 'w')

    return (f, o)

if __name__ == "__main__":
    main()


