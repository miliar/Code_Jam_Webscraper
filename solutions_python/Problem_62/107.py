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

_debug = 0



def solve_case(case_no,  N, wires_l   ):
    print "-------------- New case", case_no

    # sort wires by Ai
    wires_l.sort(key=lambda t:t[0])

    print wires_l

    bi_l=[i[1] for i in wires_l]
    bi_sorted_l = bi_l[:]
    bi_sorted_l.sort()

    def get_rank(b):
        bi_sorted_l.index(b)


    nb_cross=0
    for n in range(N):
        a, b = wires_l[n]

        b_rank = bi_sorted_l.index(b)
        nb_cross += abs(b_rank)

        bi_sorted_l.remove(b)
#        bi_l.remove(b)

    return nb_cross


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        N= int(fd.readline().strip())

        wires_l = []
        for _ in range(N):
            wires_l.append( [int(item) for item in fd.readline().split()] )


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, N, wires_l)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
