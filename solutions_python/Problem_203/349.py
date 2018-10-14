
from __future__ import division
import sys
import math

input = open('input.in')
output = open('out', 'wb')


class gcj:
    IN = input
    number = 0

    @classmethod
    def case(cls):
        cls.number += 1
        return 'Case #%d: ' % cls.number

    @classmethod
    def line(cls, type=str):
        line = cls.IN.readline()
        return type(line.strip('\n'))

    @classmethod
    def split_line(cls, type=str):
        line = cls.IN.readline()
        # print line
        return [type(x) for x in line.split()]

def solve(cake, R, C):
    for i in xrange(R):
        for j in xrange(C):
            if cake[i][j] != '?':
                for k in xrange(j):
                    cake[i][k] = cake[i][j]
                break
        initial = '?'
        for k in xrange(C):
            if cake[i][k] != '?':
                initial = cake[i][k]
            else:
                cake[i][k] = initial


    for i in xrange(C):
        for j in xrange(R):
            if cake[j][i] != '?':
                for k in xrange(j):
                    cake[k][i] = cake[j][i]
                break
        initial = '?'
        for k in xrange(R):
            if cake[k][i] != '?':
                initial = cake[k][i]
            else:
                cake[k][i] = initial

def main():
    t = gcj.line(int)

    for i in xrange(t):
        R, C = gcj.split_line(int)
        cake = []
        for j in xrange(R):
            cake.append(list(gcj.line()))
        output.write(gcj.case() + '\n')
        solve(cake,R,C)
        for j in xrange(R):
           output.write(''.join(cake[j]) + '\n')

    input.close()
    output.close()


if __name__ == '__main__':
    main()
