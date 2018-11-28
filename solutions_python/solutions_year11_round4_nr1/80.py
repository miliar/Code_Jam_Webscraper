#!/usr/bin/python2

"""
  Google Code Jam 2011
  Philfifi  --  http://www.pluc.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
from fractions import *
getcontext().prec = 100

#import psyco
#psyco.full()

_debug = 0



def solve_case(case_no, X, S, R, t, w    ):
    print "-------------- New case", case_no
    print X, S, R, t

    # sort by speed, slowest first


    dist_speed = []

    time_lapse = Fraction(0)
    d_togo = X

    sum_d_walkways = 0
    for B, E, speed_w in w:
        sum_d_walkways += E -B

    if X-sum_d_walkways:
        w.append((0, X - sum_d_walkways, 0))

    w.sort(key=lambda x:x[2])
#    print w


    for B, E, speed_w in w:
        d = E - B

        t = Fraction(t)

        d_run = 0

        if t > 0:
            speed_if_run = speed_w + R

            max_dist_if_run = speed_if_run * t

            d_run = min(d, max_dist_if_run)
            d_togo -= d_run
            time_run = Fraction( d_run ,   speed_if_run )
            time_lapse += time_run
            t -= time_run

#            print "run for", time_run, "seconds", d_run, "meters"

        d_walk = d - d_run
        if d_walk:
            d_togo -= d_walk
            speed_if_walk = speed_w + S
            time_lapse += Fraction( d_walk ,  speed_if_walk )
#            print "walk for", Fraction( d_walk ,  speed_if_walk ), "seconds", d_walk, "meters"

    assert d_togo == 0, "bad"

#    print "remaning run time", t

#    print time_lapse
    return time_lapse


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        X, S, R, t, N = [int(item) for item in fd.readline().split()]

        w = [None] * N

        for i in range(N):
            w[i] = [int(item) for item in fd.readline().split()]


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %.9f\n" % (case_no,
                                         solve_case(case_no,X, S, R, t, w )
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
