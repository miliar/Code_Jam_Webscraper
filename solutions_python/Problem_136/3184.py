#!/usr/bin/env python2.7

import copy as cp
import sys


class Cookieverse():
    def __init__(self, cost_per_farm, production_per_farm):
        self.cookies = self.farms = self.elapsed = 0.0
        self.cost_per_farm = cost_per_farm
        self.production_per_farm = production_per_farm

    def __repr__(self):
        return "Cookieverse(cookies={}, farms={}, elapsed={}, cps={})" \
            .format(self.cookies, self.farms, self.elapsed, self.cps)

    def buy_farm(self):
        # assert self.cookies >= self.cost_per_farm, 'not enough cookies'
        self.farms += 1.0
        self.cookies -= self.cost_per_farm

    def advance(self, dt):
        self.cookies += dt * self.cps
        self.elapsed += dt

    def advance_and_buy_farm(self):
        self.advance(self.time_to_next_farm)
        self.buy_farm()

    def advance_to_cookie_count(self, count):
        self.advance(self.time_to_cookie_count(count))

    @property
    def cps(self):
        return 2 + self.production_per_farm * self.farms

    @property
    def time_to_next_farm(self):
        return self.cost_per_farm / self.cps

    def time_to_cookie_count(self, count):
        return (count - self.cookies) / self.cps


def solve(cost_per_farm, production_per_farm, goal):
    c = Cookieverse(cost_per_farm, production_per_farm)

    while True:
        next_farm = c.time_to_next_farm
        c2 = cp.copy(c)
        c2.advance_and_buy_farm()

        t1 = c.time_to_cookie_count(goal)
        t2 = next_farm + c2.time_to_cookie_count(goal)
        if t1 > t2:
            c = c2
        else:
            c.advance_to_cookie_count(goal)
            break
    return c.elapsed


def read_case(f):
    return [float(x) for x in f.readline().split()]

filename = sys.argv[1]

with open(filename) as f:
    n_cases = int(f.readline())
    for i in xrange(n_cases):
        case = read_case(f)
        print "Case #{}: {:.7f}".format(i + 1, solve(*case))
