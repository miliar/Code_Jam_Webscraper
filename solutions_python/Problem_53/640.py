#!/usr/bin/env python

import sys

class SnapperChain(object):
    def __init__(self, input_file):
        self.input_file = input_file
        self.bits = {}

    def prepare_bits(self, max):
        for i in xrange(1, max+1):
            bit = 0
            for p in xrange(0, i):
                bit |= (1 << p)

            self.bits[i] = bit

    def solve(self):
        input = open(self.input_file, 'r')
        out = self.input_file.replace('in', 'out')
        output = open(out, 'w')

        case = int(input.readline().strip())

        for i in xrange(1, case+1):
            options = input.readline().strip().split(' ', 2)
            K = int(options[0])
            N = int(options[1])

            bit = self.bits.get(K)
            if (bit & N) == bit:
                bulb = "ON"
            else:
                bulb = "OFF"

            output.write("Case #%i: %s\n" % (i, bulb))

        input.close()
        output.close()

if __name__ == '__main__':
    problem = SnapperChain('A-large.in')
    problem.prepare_bits(30) # 1 <= N <= 30
    problem.solve()
