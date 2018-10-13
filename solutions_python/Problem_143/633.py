__author__ = 'cheungkt'

import sys


def main():
    with open(sys.argv[1], 'r') as test:
        for i in range(1, int(test.readline()) + 1):
            A, B, K = [int(x) for x in test.readline().split(' ', 2)]
            pairs = 0
            for j in range(A):
                for k in range(B):
                    if (j & k) < K:
                        pairs += 1
            print "Case #%i: %i" % (i, pairs)


if __name__ == '__main__':
    main()