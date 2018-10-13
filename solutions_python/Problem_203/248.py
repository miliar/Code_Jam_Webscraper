# -*- coding: utf-8 -*-
#!python3

__author__ = 'lostcoaster'

from trivial.codejam_thingy.files import Problem

class Cake(Problem):
    def __init__(self):
        super(Cake, self).__init__('A-large')

    def solve(self, fin):
        r, c = (int(x) for x in fin.readline().strip().split(' '))
        grid = []
        for i in range(r):
            line = list(fin.readline().strip())
            grid.append(line)

        # top left to bottom right
        for i in range(r):
            line = grid[i]
            for j in range(c):
                if line[j] == '?':
                    if j > 0 and line[j-1] != '?':
                        line[j] = line[j-1]
            if line[c-1] == '?' and i > 0:
                # empty line, we copy previous line
                for j in range(c):
                    line[j] = grid[i-1][j]

        # reverse
        for i in range(r):
            line = grid[r-1-i]
            for j in range(c):
                if line[c-1-j] == '?':
                    if j > 0 and line[c-j] != '?':
                        line[c-1-j] = line[c-j]
            if line[0] == '?' and i > 0:
                # empty line, we copy previous line
                for j in range(c):
                    line[j] = grid[r-i][j]

        out = ''
        for i in range(r):
            out += '\n' + ''.join(grid[i])
        return out

if __name__ == '__main__':
    Cake().run()

