__author__ = 'msufa'

import sys


class InputFileParser(object):
    def __init__(self, filename):
        self.test_cases = []
        with open(filename, 'r') as in_f:
            self.test_case_count = int(in_f.readline())
            for i in xrange(1, self.test_case_count + 1):
                tc = TestCase(i)
                tc.x, tc.r, tc.c = [int(val) for val in in_f.readline().strip().split(' ')]
                self.test_cases.append(tc)


class TestCase(object):
    def __init__(self, index):
        self.index = index
        self.x = 0
        self.r = 0
        self.c = 0


if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit('input and output file not specified!')

    parser = InputFileParser(sys.argv[1])
    with open(sys.argv[2], 'w') as out_f:
        for tc in parser.test_cases:
            if (tc.r * tc.c) % tc.x != 0:
                winner = 'RICHARD'
            elif tc.x > tc.r and tc.x > tc.c:
                winner = 'RICHARD'
            elif ((tc.r * tc.c) / tc.x) < tc.x - 1:
                winner = 'RICHARD'
            else:
                winner = 'GABRIEL'
            # print 'Case #{0}: {1}'.format(tc.index, winner)
            out_f.write('Case #{0}: {1}\n'.format(tc.index, winner))
