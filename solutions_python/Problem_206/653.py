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

def solve(data, D):
    t = []
    for entry in data:
        t.append((D-entry[0])/entry[1])
    return '%.6f' % (D/max(t))


def main():
    t = gcj.line(int)
    for _ in xrange(t):
        D, N = gcj.split_line(int)
        data = []
        for i in xrange(N):
            data.append(gcj.split_line(int))
        output.write(gcj.case() + solve(data, D) + '\n')
    input.close()
    output.close()

if __name__ == '__main__':
    main()
