__author__ = 'bowen'

from os.path import splitext
from sys import setrecursionlimit
from math import *

setrecursionlimit(10000)


class MetaClass(type):
    def __init__(cls, name, bases, d):
        type.__init__(cls, name, bases, d)
        #cls.static_variable =


class Solver(object):
    __metaclass__ = MetaClass

    def __init__(self, case_input):
        self.A, self.B, self.K = [int(item) for item in case_input.readline().strip().split(' ')]

    def solve(self):
        count = 0
        for i in xrange(self.A):
            for j in xrange(self.B):
                if i & j < self.K:
                    count += 1
        return count

    def get_result(self):
        result = self.solve()
        #format result to text
        result = '%d' % result
        return result


def main(case_input, case_output):
    T = int(case_input.readline())
    for i in xrange(1, T + 1):
        result = Solver(case_input).get_result()
        print 'Case #%d: %s' % (i, result)
        case_output.write('Case #%d: %s\n' % (i, result))

current_path = splitext(__file__)[0]
input_path = current_path + '.in'
output_path = current_path + '.out'

with open(output_path, 'w') as outfile:
    with open(input_path, 'r') as infile:
        main(infile, outfile)