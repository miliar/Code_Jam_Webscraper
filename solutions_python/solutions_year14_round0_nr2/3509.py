#!/usr/bin/env python3

import sys
import argparse
from decimal import *

getcontext().prec = 10


def parse_args():
    """
    Handle command-line arguments.
    """
    parser = argparse.ArgumentParser(description=__doc__,
                                     fromfile_prefix_chars='@')
    parser.add_argument('infile',
                        type=argparse.FileType('r'), nargs='?',
                        default=sys.stdin, help='input file')
    parser.add_argument('outfile',
                        type=argparse.FileType('w'), nargs='?',
                        default=sys.stdout, help='output file')
    return parser.parse_args()


class Player(object):
    def __init__(self, c, f, x):
        self.cookies = Decimal(0)
        self.rate = Decimal(2)
        self.farms = 0
        self.time = Decimal(0)

        self.farm_cost = c
        self.farm_rate = f
        self.end = x

    def buy_farm(self):
        self.farms += 1
        self.cookies -= self.farm_cost
        self.rate += self.farm_rate

    def increment(self, d_time):
        self.time += d_time
        d_cookies = self.rate * d_time
        self.cookies += d_cookies

    def time_to_x(self, cookies, rate):
        return (self.end - cookies) / rate

    def do_next(self):
        if self.cookies + self.farm_cost >= self.end:
            self.increment(self.time_to_x(self.cookies, self.rate))
            return True
        else:
            self.increment(self.farm_cost / self.rate)
            self.decide_farm()
            return False

    def decide_farm(self):
        c_yesfarm = self.cookies - self.farm_cost
        r_yesfarm = self.rate + self.farm_rate
        t_yesfarm = self.time_to_x(c_yesfarm, r_yesfarm)

        t_nofarm = self.time_to_x(self.cookies, self.rate)

        if t_yesfarm < t_nofarm:
            self.buy_farm()


def parse_line(line):
    return [Decimal(i) for i in line.split(' ', 2)]


def solve(case):
    c, f, x = parse_line(next(case))
    p = Player(c, f, x)

    done = False
    while not done:
        done = p.do_next()

    return p.time


def main():
    args = parse_args()

    with args.infile as infile, args.outfile as outfile:
        infile = (line.rstrip() for line in infile)
        n = int(next(infile))

        for c in range(n):
            s = solve(infile)
            outstr = "Case #{:d}: {}".format(c + 1, s)
            print(outstr, file=outfile)


if __name__ == '__main__':
    exit = main()
    if exit:
        sys.exit(exit)
