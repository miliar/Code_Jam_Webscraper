__author__ = 'Antariksh Bothale'

import sys

if __name__ == '__main__':
    lines = sys.stdin.readlines()

    lines = lines[1:]
    case_num = 0
    for line in lines:
        good = set()
        A,B,K = map(int, line.strip().split())

        for a in xrange(0, A):
            for b in xrange(0, B):
                if (a&b) < K:
                    good.add((a, b))
        case_num += 1
        print 'Case #{0}: {1}'.format(case_num, len(good))

