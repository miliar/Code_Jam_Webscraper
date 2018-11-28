#!/usr/bin/python


import math
from optparse import OptionParser
import sys


def solve(t, fin):
    S, K = fin.readline().split()
    K = int(K)
    S = list(S)

    count = 0
    for i in xrange(len(S) - K + 1):
        if S[i] == '-':
            for k in xrange(K):
                if S[i+k] == '+':
                    S[i+k] = '-'
                else:
                    S[i+k] = '+'
            count += 1
    for i in xrange(len(S) - K + 1, len(S)):
        if S[i] == '-':
            ans = 'IMPOSSIBLE'
            break
    else:
        ans = count

    print('Case #{}: {}'.format(t, ans))


def main():
    parser = OptionParser()
    parser.add_option('-i', '--input', help='Input file')
    opts, args = parser.parse_args()

    if opts.input is not None:
        fin = open(opts.input, 'r')
    else:
        fin = sys.stdin

    T = int(fin.readline())
    for t in xrange(1, T+1):
        solve(t, fin)

    fin.close()


if __name__ == '__main__':
    main()


