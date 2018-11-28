#!/usr/bin/env python
import sys
if __name__ == "__main__":
    input = open(sys.argv[1])
    T = int(input.readline())
    for ncase in xrange(1, T + 1):
        c, f, x = map(float, input.readline().split())
        n = 0
        t = 0.0
        min_t = x / 2.0
        while True:
            t += c / (2.0 + n * f)
            n += 1
            cur_t = t + x / (2.0 + n * f)
            if cur_t > min_t:
                break
            else:
                min_t = cur_t
        print "Case #%d: %.8lf" % (ncase, min_t)
