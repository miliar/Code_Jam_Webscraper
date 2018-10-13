#!/usr/bin/env python

import re

outf = 'out.txt'

def eq(a, b, eps=0.0000001):
    return abs(a - b) <= eps

class CookieClicker(object):

    def __init__(self, pid, fo):
        self.c = None
        self.f = None
        self.x = None
        self.r = 2
        self.pid = pid
        self.fo = fo

    def read_params(self, *args):
        self.c = args[0]
        self.f = args[1]
        self.x = args[2]

    def result(self, flt):
        string = "Case #" + str(self.pid) + ": " + "%0.7f" % flt
        return string

    def t_for_nth_buy(self, n):
        return self.c / (self.r + self.f * (n - 1))

    def t_n_buy(self, n):
        t = 0.0
        for i in range(1, n + 1):
            t += self.t_for_nth_buy(i)
        t += (self.x) / (self.r + self.f * n)
        return t

    def t_n_from_nm(self, n, tnm):
        if n == 0:
            t = self.t_n_buy(n)
        else:
            t = tnm - (self.x) / (self.r + self.f * (n - 1))
            t += self.t_for_nth_buy(n)
            t += (self.x) / (self.r + self.f * n)
        return t

    def solve(self):
        if self.x < self.c or eq(self.x, self.c):
            max_buy = 0
        else:
            gnd = int(self.x / self.c - self.r / self.f - 1)
            if gnd < 0:
                max_buy = 0
            else:
                max_buy = gnd + 1
        n = 0
        t = 0.0
        if max_buy == 0:
            t = self.t_n_buy(0)
        else:
            for i in range(max_buy + 1):
                tmpt = self.t_n_from_nm(n, t)
                if n > 0:
                    if tmpt > t or eq(tmpt, t):
                        break
                t = tmpt
                n += 1
        self.fo.write(self.result(t) + "\n")

    def test_print(self):
        print "C:", self.c, "F:", self.f, "X:", self.x


def read_and_solve(pid, fo):
    cco = CookieClicker(pid, fo)
    pl = [float(x) for x in re.split(r'\s+', raw_input().strip())]
    cco.read_params(*pl)
    cco.solve()


def main():
    with open(outf, 'w') as fo:
        n = int(raw_input())
        ndone = 0
        while ndone < n:
            try:
                # 1-based numbering
                read_and_solve(ndone + 1, fo)
                ndone += 1
            except EOFError:
                break


if __name__ == "__main__":
    main()
