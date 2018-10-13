#!/usr/bin/env python
import sys


def main():
    file_in = open("A-small-attempt0.in")
    file_out = open("A-small.out", "w")
    #file_out = sys.stdout
    n_tests = int(file_in.readline())
    for i in xrange(n_tests):
        n, A, B, C, D, x0, y0, M = map(int, file_in.readline().split())
        coord = []
        X = x0
        Y = y0
        coord.append((X, Y))
        for j in xrange(1, n):
            X = (A * X + B) % M
            Y = (C * Y + D) % M
            coord.append((X, Y))
        cnt = 0;
        for a1 in xrange(len(coord)-2):
            for a2 in xrange(a1+1, len(coord)-1):
                for a3 in xrange(a2+1, len(coord)):
                    if (coord[a1][0]+coord[a2][0]+coord[a3][0]) % 3 == 0 and \
                        (coord[a1][1]+coord[a2][1]+coord[a3][1]) % 3 == 0:
                            cnt += 1

        print >> file_out, "Case #%d: %d" % (i+1, cnt)

    #file_out.close()
    #file_in.close()
if __name__ == '__main__':
    main()