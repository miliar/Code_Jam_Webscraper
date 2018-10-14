# -*- coding: utf-8 -*-
#!python3

__author__ = 'lostcoaster'

from trivial.codejam_thingy.files import Problem

class Cores(Problem):
    def __init__(self):
        super(Cores, self).__init__('C-small-1-attempt1')

    def solve(self, in_file):
        n, k = (int(x) for x in in_file.readline().split())
        v = float(in_file.readline())
        p = [float(x) for x in in_file.readline().split()]

        if n == 1:
            return min(1.0, p[0] + v)

        p.sort()
        ori_p = p[:]
        while v > 0:
            for i in range(n):
                if p[i] > p[0]:
                    break
            else:
                v /= n
                for k in range(n):
                    p[k] = min(1.0, p[k] + v)
                break
            if v/i <= p[i] - p[0]:
                for k in range(i):
                    p[k] += v/i
                v = 0
            else:
                v -= (p[i]-p[0]) * i
                for k in range(i):
                    p[k] = p[i]

        ret = 1
        print(f'{ori_p} to {p}')
        for pp in p:
            ret *= pp
        return ret

if __name__ == '__main__':
    Cores().run()
