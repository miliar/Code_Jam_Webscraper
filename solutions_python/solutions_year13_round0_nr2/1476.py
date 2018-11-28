#! /usr/bin/python3.2
# -*- coding: UTF-8 -*-

from sys import argv

class Lawn:

    def sum_y(self, y):
        if y in self.cachy: return self.cachy[y]
        s = sum(self.matrix[y])/self.width
        self.cachy[y] = s
        return s

    def sum_x(self, x):
        if x in self.cachx: return self.cachx[x]
        s = sum(self.matrix[i][x] for i in range(0, self.height))/self.height
        self.cachx[x] = s
        return s

    def __init__(self, lines):
        self.matrix = [ [ int(i) for i in l.split(' ') ] for l in lines ]
        self.height = len(self.matrix)
        self.width  = len(self.matrix[0])
        self.cachy  = {}
        self.cachx  = {}

    def is_ok(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if not self.verify(y, x):
                    return 'NO'

        return 'YES'

    def verify(self, y, x):
        me = self.matrix[y][x]

        if me == 2:
            return True

        if self.sum_y(y) == me:
            return True

        return self.sum_x(x) == me


if __name__ == '__main__':
    f = open(argv[1], 'r')
    count, *lines = f.readlines()
    f.close()
    lines = [ l.replace('\n', '') for l in lines ]
    cursor = 0
    f = open('lawnmower.output', 'w')
    for case in range(1, int(count)+1):
        f.write('Case #' + str(case) + ': ')
        height = int(lines[cursor].split(' ')[0])
        cursor += 1
        l = Lawn([ lines[cursor+i] for i in range(0, height) ])
        f.write(l.is_ok() + '\n')
        cursor += height

    f.close()
