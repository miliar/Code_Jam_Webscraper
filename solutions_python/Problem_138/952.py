#!/usr/bin/env python
import sys
if __name__ == "__main__":
    input = open(sys.argv[1])
    T = int(input.readline())
    for ncase in xrange(1, T + 1):
        num_weights = int(input.readline())
        naomi = sorted(map(float, input.readline().split()))
        ken = sorted(map(float, input.readline().split()))
        assert(len(naomi) == num_weights)
        assert(len(ken) == num_weights)
        kf = 0
        nf = 0
        deceit = 0
        for i in xrange(num_weights):
            if naomi[nf] > ken[kf]:
                deceit += 1
                nf += 1
                kf += 1
            else:
                nf += 1
        war = 0
        kt = num_weights - 1
        nt = num_weights - 1
        for i in xrange(num_weights):
            if naomi[nt] > ken[kt]:
                nt -= 1
                war += 1
            else:
                nt -= 1
                kt -= 1
        print "Case #%d:" % ncase, deceit, war
