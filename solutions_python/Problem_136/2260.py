#!/usr/bin/python3

import sys
import math

class Case(object):
    def __init__(self, case_id):
        self.case_id = case_id
        self.last_farms = None

    def eta_build_farms(self, farms):
        if farms == 0:
            return (2., 0.)

        if self.last_farms == farms:
            return self.last_results

        (rate, time) = self.eta_build_farms(farms - 1)

        time += self.C / rate
        rate += self.F

        self.last_farms = farms
        self.last_results = (rate, time)

        return (rate, time)

    def eta(self, f):
        (rate_f, eta_f) = self.eta_build_farms(f)
        return self.X / rate_f + eta_f

    def solve_case(self):
        last_eta = 100000000
        f = 0
        while True:
            eta = self.eta(f)

            if last_eta > eta:
                last_eta = eta
            else:
                self.time_cookies = last_eta
                return last_eta

            f+=1

    def __str__(self):
        return str(self.C) + ' ' + str(self.F) + ' ' + str(self.X)

    def read_case(self, f):
        (self.C, self.F, self.X) = [float(x) for x in f.readline().strip().split(' ')]

    def print_solution(self, o):
        print('Case #%d: ' % (self.case_id), file=o, end='')
        print(self.time_cookies, file=o)

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


