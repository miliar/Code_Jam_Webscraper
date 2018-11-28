#!/usr/bin/env pypy

INPUT_FILE = 'sample.in'
INPUT_FILE = 'B-small-attempt0.in'


def solve(A, B, K):
    res = 0
    for i in range(A):
        for j in range(B):
            if i & j < K:
                res += 1
    return res


def main():
    fp = open(INPUT_FILE, 'r')
    NUM_TESTS = int(fp.readline())
    for nt in range(NUM_TESTS):
        A, B, K = [int(x) for x in fp.readline().strip().split(' ')]

        res = solve(A, B, K)

        print 'Case #%d:' % (nt + 1),
        print res


if __name__ == '__main__':
    main()
