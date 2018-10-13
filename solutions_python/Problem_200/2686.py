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


def is_tidy(num):
    num_str = str(num)
    if len(num_str) == 1:
        return True

    for i in xrange(1, len(num_str)):
        if num_str[i] < num_str[i-1]:
            return False

    return True

def solve(N):
    for i in xrange(N, 0, -1):
        if is_tidy(i):
            return i


def main():
    t = gcj.line(int)

    for i in xrange(t):
        N = gcj.line(int)
        output.write(gcj.case() + str(solve(N)) + '\n')

    input.close()
    output.close()


if __name__ == '__main__':
    main()
