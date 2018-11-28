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



def solve_case(case_no, s_max, s_d    ):
    print "-------------- New case", case_no

    nb_invite = 0
    nb_up = 0

    for s in range(s_max+1):
        missing = s - nb_up
        if missing <= 0: # they stand up
            pass
        else:
            nb_invite += missing
            nb_up += missing
        nb_up += s_d[s]


    return nb_invite


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        s_max, k_s = fd.readline().split()
        s_max = int(s_max)

        s_d = {}

        s_cur = 0
        for s in k_s:
            s_d[s_cur] = int(s)
            s_cur += 1

        assert s_max == s_cur-1

        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, s_max, s_d)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
