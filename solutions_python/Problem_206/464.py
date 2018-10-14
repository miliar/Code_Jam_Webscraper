# -*- coding: utf-8 -*-
#!python3

__author__ = 'lostcoaster'

from trivial.codejam_thingy.files import Problem


class Pony(Problem):
    def __init__(self):
        super(Pony, self).__init__('A-large')

    def solve(self, in_file):
        d, n = (int(x) for x in in_file.readline().strip().split(' '))
        t = None
        zero = False
        for i in range(n):
            k, s = (int(x) for x in in_file.readline().strip().split(' '))
            m = (d-k)/s
            if t is None or m > t:
                t = m
        return d/t

if __name__ == '__main__':
    Pony().run()


