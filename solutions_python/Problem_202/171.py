#!python3
# -*- coding: utf-8 -*-

__author__ = 'lostcoaster'

import trivial.codejam_thingy.files as f


class Fashion(f.Problem):
    def __init__(self):
        super(Fashion, self).__init__('D-small-attempt1')

    def solve(self, fin):
        # init
        n, m = (int(x) for x in fin.readline().strip().split(' '))

        # the problem is essentially :
        # n-rook problem with 'x' and n-bishop problem with '+'
        # we just need to find the solution of them separately, and "merge" them, where the overlapping point
        # is replaced with 'o'
        row = set(i for i in range(1, n+1))
        col = set(i for i in range(1, n+1))
        rcsum = set(i for i in range(2, n*2+1))
        rcsub = set(i for i in range(1-n, n))
        points = {}
        style = 0
        pcount = 0

        for line in range(m):
            c, x, y = fin.readline().strip().split(' ')
            x = int(x)
            y = int(y)
            points[x, y] = c
            if c == 'o' or c == '+':
                rcsum.remove(x + y)
                rcsub.remove(x - y)
                style += 1
            if c == 'o' or c == 'x':
                row.remove(x)
                col.remove(y)
                style += 1
        orig_points = points.copy()

        while len(row) > 0:
            p = row.pop(), col.pop()  # any x, y combination is valid
            if p in points:
                assert points[p] == '+', 'sanity check failed!'
                points[p] = 'o'
            else:
                points[p] = 'x'
            style += 1

        # n-bishop is so much harder than n-rook, wow
        # loop from shortest diagonals
        for d in range(n):
            dx = (1-n+d, n-1-d)
            dy = (n+1-d, n+1+d)
            for i in dx:
                for j in dy:
                    if i in rcsub and j in rcsum:
                        rcsub.remove(i)
                        rcsum.remove(j)
                        p = (i+j)//2, (j-i)//2
                        if p in points:
                            assert points[p] == 'x', 'sanity check 2 failed!'
                            points[p] = 'o'
                        else:
                            points[p] = '+'
                        style += 1

        output_lines = ''
        for p in points:
            if p not in orig_points or points[p] != orig_points[p]:
                pcount += 1
                output_lines += f'\n{points[p]} {p[0]} {p[1]}'
        return f'{style} {pcount}'+output_lines

if __name__ == '__main__':
    Fashion().run()
