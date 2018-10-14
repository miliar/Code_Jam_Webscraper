
import logging
import os
import sys

import argparse


class Case(object):
    def __init__(self, n, N):
        self.n = n
        self.N = N
        self.r = n

    def solve(self):
        logging.info('solving for #%d ...', self.n)

        def check(v):
            r = 10
            while v != 0:
                r0 = v % 10
                if r0 > r:
                    return False
                r = r0
                v /= 10

            return True

        N = self.N
        # i = N.find('0')
        # if i != -1:
        #     N = N[0] + ('0' * (i-1)) + N[i:]

        N = long(N)
        while N > 0 and not check(N):
            N -= 1

        self.r = N

    @property
    def result(self):
        return 'Case #{0}: {1}'.format(self.n, self.r)


parser = argparse.ArgumentParser()
parser.add_argument('--output-file', default=None)
parser.add_argument('input_file', nargs=1)
arguments = parser.parse_args()

logging.basicConfig(level=logging.INFO)

output = sys.stdout if arguments.output_file is None else open(arguments.output_file, 'w')

with open(arguments.input_file[0]) as input_file:
    T = int(input_file.readline().strip())
    for i, l in enumerate(input_file):
        c = Case(i+1, l.strip())
        c.solve()
        output.write(c.result)
        output.write(os.linesep)