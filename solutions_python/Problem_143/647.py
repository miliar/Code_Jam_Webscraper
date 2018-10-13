import math
import sys


if __name__ == '__main__':
    stdin = sys.stdin
    num_cases = stdin.readline()

    for i in range(int(num_cases)):
        winners = 0
        line = stdin.readline()
        A, B, K = map(int, line.split())

        for a in range(A):
            for b in range(B):
                if (a & b) < K:
                    winners += 1

        print "Case #%d: %d" % (i+1, winners)

