#!/usr/bin/python
# Python 2.6

import sys
import math

def dist(p1, p2):
    a, b, c = p1
    x, y, z = p2
    m = a - x
    n = b - y
    mm = m * m
    nn = n * n
    return math.sqrt(mm + nn)


def main(infile):
    T = infile.int()
    for t in xrange(T):

        N = infile.int()

        points = []

        for n in xrange(N):

            X, Y, R = infile.ints()
            points.append((X, Y, R))

        if N == 1:
            result = points[0][2]

        elif N == 2:
            result = max(r for (x, y, r) in points)

        else:
            points = sorted(points, lambda a, b: cmp(a[2], b[2]))
            options = []

            # taking 1

            for i, p in enumerate(points):

                rest = points[:]
                del rest[i]

                r = p[2]

                p1 = rest[0]
                p2 = rest[1]

                d = dist(p1, p2)
                r1 = p1[2]
                r2 = p2[2]
                full = r1 + d + r2
                half = full / 2.0

                if r >= half:
                    options.append(r)

                options.append(half)

            # taking all

            result = min(options)

        print "Case #{0}: {1}".format(t+1, result)


class FileReader:
    def __init__(self, file):
        self.file = file

    def string(self):
        return self.file.readline().rstrip()

    def strings(self):
        return self.string().split()

    def int(self):
        return int(self.string())

    def ints(self):
        return map(int, self.strings())

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        main(FileReader(f))

