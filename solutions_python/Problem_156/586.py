#!/usr/bin/python2

"""
  Google Code Jam 2015
  Philfifi  --  http://www.pluc.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

#import psyco
#psyco.full()

_debug = 0

def nb_special_for_P_max(P_max, P_l):
    nb_spec = 0

    for P in P_l:
        if P <= P_max:
            break

        a, b = divmod(P, P_max)
#        print "a b", a, b
        nb_spec += a-1
        if b:
            nb_spec += 1

#        print "tmp", nb_spec

    return nb_spec



def solve_case(case_no, D, P_l    ):
    print "-------------- New case", case_no

    print P_l

    m = max(P_l)


    soluc_min = m


    for P_max in range(1, m+1):
#        print "P_max =", P_max
        n = nb_special_for_P_max(P_max, P_l)
#        print "nb_spec =", n
        soluc = P_max + n
        print "soluc", soluc

        if soluc < soluc_min:
            soluc_min = soluc

    return soluc_min

def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        D = int(fd.readline())
        P_l = sorted([int(item) for item in fd.readline().split()], reverse=True)


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, D, P_l)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
