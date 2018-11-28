import math
import sys


def parse(f):
    X, R, C = map(int, f.readline().strip().split())

    return X, R, C

# Computed by hand.
TABLE = set([(4, 4, 4), (2, 4, 4), (1, 4, 4),
             (4, 4, 3), (3, 4, 3), (2, 4, 3), (1, 4, 3),
             (2, 4, 2), (1, 4, 2),
             (2, 4, 1), (1, 4, 1),
             (3, 3, 3), (1, 3, 3),
             (3, 3, 2), (2, 3, 2), (1, 3, 2),
             (1, 3, 1),
             (2, 2, 2), (1, 2, 2),
             (2, 2, 1), (1, 2, 1),
             (1, 1, 1)])


def solve(X, R, C):
    return (X, max(R,C), min(R,C)) in TABLE


def main():
    with open(sys.argv[1], "r") as input_file:
        T = int(input_file.readline())

        for i in xrange(T):
            X, R, C = parse(input_file)
            if solve(X, R, C):
                result = "GABRIEL"
            else:
                result = "RICHARD"

            print "Case #%d: %s" % (i+1, result)


if __name__ == "__main__":
    main()
