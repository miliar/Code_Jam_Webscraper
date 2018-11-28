#!/usr/bin/env python
# encoding: utf-8
import math
import sys

__author__ = 'rui'

cases = []
dataset = 'B-large'


class TestCase(object):
    def __init__(self, id, plates, pancakes):
        self.id = id
        self.plates = plates
        self.pancakes = pancakes

    def solve(self):
        ret = max(self.pancakes)
        for t in range(1, max(self.pancakes)):
            try_ret = t
            for plate in self.pancakes:
                if plate > t:
                    try_ret += plate / t - 1 if plate % t == 0 else plate / t
            ret = min(ret, try_ret)
        return 'Case #%d: %d' % (self.id, ret)

    def __str__(self):
        return '%d\t%s' % (self.id, self.pancakes)


if __name__ == '__main__':
    with open(dataset + '.in') as f:
        lines = f.readlines()
        size = int(lines[0])
        id = 1
        for i in range(0, len(lines[1:]) / 2):
            plates = lines[i * 2 + 1].strip()
            pancakes = map(int, lines[i * 2 + 2].strip().split(' '))
            cases.append(TestCase(id, plates, pancakes))
            id += 1

    f = open(dataset+'.out','w')
    for case in cases:
        print case
        ret = case.solve()
        print ret
        print ''
        f.write(ret + '\n')
