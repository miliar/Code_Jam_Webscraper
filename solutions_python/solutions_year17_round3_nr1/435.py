# -*- coding: utf-8 -*-
import sys
from math import pi

class Pancake(object):
    def __init__(self, R, H):
        self.R = R
        self.H = H

    @property
    def areaH(self):
        return 2*pi*self.H*self.R

    @property
    def areaS(self):
        return pi*self.R**2

    @property
    def total(self):
        return self.areaH + self.areaS


def get_stack_score(init, pancakes, nb):
    pancakes = sorted(pancakes, key=lambda p:-p.areaH)
    return init + sum(p.areaH for p in pancakes[:nb])


def solve(pancakes, N, K):
    pancakes = sorted(pancakes, key=lambda p: -p.R)
    max_score = 0
    for j in xrange(0, N-K+1):
        score = get_stack_score(
            init=pancakes[j].total,
            pancakes=pancakes[j+1:],
            nb=K-1
        )

        if score > max_score:
            max_score = score

    return max_score


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        n_cases = int(f.readline())
        for i in xrange(n_cases):
            N, K = map(int,f.readline().split())
            pancakes = []
            for j in xrange(N):
                R,H = map(int,f.readline().split())
                pancakes.append(Pancake(R=R, H=H))

            res = solve(pancakes, N, K)
            print 'Case #{}: {:.7f}'.format(i+1,res)
        
