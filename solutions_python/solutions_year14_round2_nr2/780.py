#!/usr/bin/python2

"""
  Google Code Jam 2014
  Philfifi  --  http://www.pluc.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

#import psyco
#psyco.full()

_debug = 0



def solve_case(case_no,  A, B, K   ):
    print "-------------- New case", case_no


    ret = 0

    if K > A or K > B:
        return A*B

    # all a < K:
    ret += (K) * B

    # all b < K:
    ret += (K) * A

    ret -= (K) * (K)


    for a in range(K, A):
        for b in range(K, B):
            if a & b < K:
                ret += 1



    return ret


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        A, B, K = [int(item) for item in fd.readline().split()]


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, A, B, K)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
