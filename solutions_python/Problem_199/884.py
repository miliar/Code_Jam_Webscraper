#!python3
# -*- coding: utf-8 -*-

__author__ = 'lostcoaster'

import trivial.codejam_thingy.files as f

class Pancake(f.Problem):
    def __init__(self):
        super(Pancake, self).__init__('A-large')

    def solve(self, fin):
        cakes, k = fin.readline().strip().split(' ')
        cakes = [c!='-' for c in cakes]
        n = len(cakes)
        k = int(k)
        p = 0
        for i in range(len(cakes)):
            if not cakes[i]:
                p += 1
                for j in range(k):
                    if i + j >= n:
                        return 'IMPOSSIBLE'
                    cakes[i+j] = not cakes[i+j]
        return str(p)

if __name__ == '__main__':
    Pancake().run()
