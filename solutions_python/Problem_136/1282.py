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



def solve_case(case_no, C, F, X    ):
    print "-------------- New case", case_no

    T = 0.
    P = 2.  # Current production rate

    target_time_at_this_rate = T + X/P

    nb_farms = 0
    while True:

        delay_next_farm = C/P
        P_after_next_farm = P + F

        target_time_with_another_farm = T + delay_next_farm + X/P_after_next_farm

#        print "target_time_with_another_farm", target_time_with_another_farm

        if target_time_at_this_rate < target_time_with_another_farm:
            print nb_farms
            return target_time_at_this_rate
        else:
            nb_farms += 1
            T += delay_next_farm
            P = 2 + nb_farms*F
            target_time_at_this_rate = target_time_with_another_farm


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        C, F, X = [float(item) for item in fd.readline().split()]


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %.7f\n" % (case_no,
                                         solve_case(case_no, C, F, X)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
