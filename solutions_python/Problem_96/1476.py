#!/usr/bin/python2

"""
  Google Code Jam 2012
  Philfifi  --  http://www.pluc.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

#import psyco
#psyco.full()

_debug = 0


def init():

    score_to_max_not_surprising = {}
    score_to_max_if_surprising = {}

    for a in range(11):
        for b in range(a, 11):
            for c in range(b, 11):
                t = (a,b,c)
                print t
                MIN = a
                MAX = c

                is_not_surprising = c-a in (0,1)
                is_surprising = c-a == 2

                score = a + b + c

                if is_not_surprising:
                    if score not in score_to_max_not_surprising:
                        score_to_max_not_surprising[score] = MAX
                    else:
                        score_to_max_not_surprising[score] = max(MAX, score_to_max_not_surprising[score])

                elif is_surprising:
                    if score not in score_to_max_if_surprising:
                        score_to_max_if_surprising[score] = MAX
                    else:
                        score_to_max_if_surprising[score] = max(MAX, score_to_max_if_surprising[score])

    print score_to_max_if_surprising, score_to_max_not_surprising
    return score_to_max_if_surprising, score_to_max_not_surprising

def solve_case(case_no,   N, S, p, t, score_to_max_if_surprising, score_to_max_not_surprising ):
    print "-------------- New case", case_no

    print "p=", p, "S=", S

    m = 0
    for score in t:

        MAX = score_to_max_not_surprising.get(score, -1)
        if MAX >= p:
            m += 1

        elif S >0:
            MAX = score_to_max_if_surprising.get(score, -1)
            if MAX >= p:
                m += 1
                S -= 1
    return m


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())

    score_to_max_if_surprising, score_to_max_not_surprising = init()

    for case_no in range(1, nb_cases+1):

        l = [int(item) for item in fd.readline().split()]
        N = l[0]
        S = l[1]
        p = l[2]
        t = l[3:]


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, N, S, p, t, score_to_max_if_surprising, score_to_max_not_surprising)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
