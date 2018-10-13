#!/usr/bin/python3

import sys
import math

class Case(object):
    def __init__(self, case_id):
        self.case_id = case_id

    def solve_case(self):
        set1 = set(self.row_set1[self.row1-1])
        set2 = set(self.row_set2[self.row2-1])
        self.guess = set1.intersection(set2)

    def __str__(self):
        return str(self.row1) + ' ' + str(self.row2) + '\n' + str(self.row_set1) + '\n' + str(self.row_set2)

    def read_case(self, f):
        self.row1 = int(f.readline().strip())
        self.row_set1 = [[int(x) for x in f.readline().strip().split(' ')] for l in range(4)]
        self.row2 = int(f.readline().strip())
        self.row_set2 = [[int(x) for x in f.readline().strip().split(' ')] for l in range(4)]

    def print_solution(self, o):
        print('Case #%d: ' % (self.case_id), file=o, end='')
        if len(self.guess) == 1:
            print(list(self.guess)[0], file=o)
        elif len(self.guess) == 0:
            print('Volunteer cheated!', file=o)
        else:
            print('Bad magician!', file=o)

def main():
    (f, o) = open_files()

    nb = int(f.readline().strip())
    for case_id in range(1, nb + 1):
        case = Case(case_id)
        case.read_case(f)
        case.solve_case()
        case.print_solution(o)

def open_files():
    if len(sys.argv) == 1:
        f = sys.stdin
        o = sys.stdout

    if len(sys.argv) == 2:
        f = open(sys.argv[1], 'r')
        o = sys.stdout

    if len(sys.argv) == 3:
        f = open(sys.argv[1], 'r')
        o = open(sys.argv[2], 'w')

    return (f, o)

if __name__ == "__main__":
    main()


