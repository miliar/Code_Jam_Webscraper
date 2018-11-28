#!/usr/bin/python3

import sys
import math

class Case(object):
    def __init__(self, case_id):
        self.case_id = case_id
        self.nb_wins = 0

    def solve_case(self):
        win = 0

        for a in range(self.A):
            for b in range(self.B):
                if a&b < self.K:
                    win += 1

        self.nb_wins = win

    def __str__(self):
        return str(self.lines)

    def read_case(self, f):
        (self.A, self.B, self.K) = [int(x) for x in f.readline().split(' ')]

    def print_solution(self, o):
        print('Case #%d: ' % (self.case_id), file=o, end='')
        print(self.nb_wins, file=o)

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


