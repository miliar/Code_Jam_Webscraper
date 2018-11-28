#!/usr/bin/python

"""
  Google Code Jam 2010
  Philfifi  --  http://www.pluc.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

import psyco
psyco.full()

from math import sqrt

_debug = 0



def solve_case(case_no, L, P, C    ):
    print "-------------- New case", case_no

    nb_tries =0
    print "L, P, C", L, P, C

    if L*C >= P:
        print 0
        return 0

    if L*C < P and (P-L == 2):
        print 1
        return 1

    while L*C < P:
        print "  L, P", L, P
        a = sqrt(L*P)
        a_int=int(a)

        if ((a_int-1) ** 2 == L*P):
            a_int = a_int -1
            print "is exact 1"
        elif ((a_int+1) ** 2 == L*P):
            a_int = a_int +1
            print "is exact 2"
        elif ((a_int) ** 2 == L*P):
            print "is exact 0"
        else:
            a_int += 1

        print "   a", a, a_int
        nb_tries += 1
        P=a_int
#        L=max(a_int,
#              L*C)

        if a <= C:
            break

    print nb_tries
    return nb_tries


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        L, P, C = [int(item) for item in fd.readline().split()]


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, L, P, C)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
