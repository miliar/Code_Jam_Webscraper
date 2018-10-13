from __future__ import division
import sys

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >=2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    no_cases = int(f.readline())
    for case in xrange(no_cases):
        c, g, x = [float(i) for i in f.readline().split()]
        time = 0.0
        rate = 2.0
        while True:
            if x / rate > c / rate + x / (rate + g):
                time += c / rate
                rate += g
            else:
                time += x / rate
                break
        print "Case #%d: %f" % (case + 1, time)