#!/usr/bin/python2

"""
  Google Code Jam 2011
  Philfifi  --  http://www.pluc.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

#import psyco
#psyco.full()

_debug = 0


def solve_case(case_no,  R,C, D, w   ):
    print "-------------- New case", case_no

#    print w

    def bari(c, r, dim):
#        print "bari", c, r, dim
        delta_c = 0
        delta_r = 0

        max_mult = (dim) /2

        mult_c = max_mult * -1

        for c_ in range(dim):

#            print "mult_c", mult_c
            mult_r = max_mult * -1
            for r_ in range(dim):
                this_r = r+r_
                this_c = c+c_
#                print "this_c, this_r", this_c, this_r
                this_w = w[this_r][this_c]
                delta_c += mult_c * this_w
                delta_r += mult_r * this_w

                mult_r += 1
                if mult_r == 0 and (dim % 2) == 0:
                    mult_r += 1
            mult_c += 1
            if mult_c == 0 and (dim % 2) == 0:
                mult_c += 1

        # remove corners
        for c_, r_, mult_c, mult_r in ( (0, 0, -1*max_mult, -1*max_mult, ),
                                        (0, dim-1, -1*max_mult, max_mult),
                                        (dim-1, 0, max_mult, -1*max_mult),
                                        (dim-1, dim-1, max_mult, max_mult)  ):
            this_r = r+r_
            this_c = c+c_
#            print "this_c, this_r", this_c, this_r
            this_w = w[this_r][this_c]
            delta_c -= mult_c * this_w
            delta_r -= mult_r * this_w

        return delta_c == 0 and delta_r == 0

    for dim in range(min(R,C), 3-1, -1):
        print "dim", dim
        for c in range(0,C-dim+1):
            for r in range(0,R-dim+1):
#                print " test blade c,r, dim", c, r, dim
                if bari(c, r, dim):
                    return dim


    return "IMPOSSIBLE"


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        R, C, D = [int(item) for item in fd.readline().split()]

        w = [None] * R
        for _ in range(R):
            w[_] = [int(item) for item in fd.readline().strip()]

        # Have read all stuff for this case:
        f_out.write( "Case #%d: %s\n" % (case_no,
                                         solve_case(case_no, R,C, D, w )
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
