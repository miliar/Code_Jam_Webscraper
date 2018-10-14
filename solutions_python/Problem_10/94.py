#!/usr/bin/env python
import sys


def main():
    file_in = open("A-large.in")
    file_out = open("A-large.out", "w")
    #file_out = sys.stdout
    n_tests = int(file_in.readline())
    for i in xrange(n_tests):
        P, K, L = map(int, file_in.readline().split())
        FREQ = map(int, file_in.readline().split())
        if len(FREQ) != L:
            raise Exception
        used = 0
        for f in FREQ:
            if f > 0:
                used += 1
        if used > P * K:
            print >> file_out, "Case #%d: Impossible" % (i+1)
            continue

        FREQ.sort()
        FREQ.reverse()
        presses = 1
        used = 0
        c = 0
        for f in FREQ:
            c += f*presses
            used += 1
            if used == K:
                used = 0
                presses += 1

        print >> file_out, "Case #%d: %d" % (i+1, c)

    #file_out.close()
    #file_in.close()
if __name__ == '__main__':
    main()