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


def solve_case(case_no, D, init_pos_l    ):
    print "-------------- New case", case_no

    print D

    pos_vendeur_l = []
    for P, V in init_pos_l:
        for _ in range(V):
            pos_vendeur_l.append(P)

    pos_vendeur_l.sort()
    pos_vendeur_init = pos_vendeur_l[:]
    print pos_vendeur_l
    nb_vendeur = len(pos_vendeur_l)

    max_move = 0
    for i in range(nb_vendeur):
        for j in range(i+1, nb_vendeur):
            pos_i = pos_vendeur_l[i]
            pos_j = pos_vendeur_l[j]

            min_d = (j-i) * D
            real_d = pos_j - pos_i

#            print "between", i, j
#            print "  pos", pos_i, pos_j


            should_move = max(0,
                              min_d - real_d)

#            print "should_move", should_move

            if should_move > max_move:
                max_move = should_move

    return max_move/2.


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        C, D = [int(item) for item in fd.readline().split()]

        init_pos_l = []
        for i in range(C):
            P, V = [int(item) for item in fd.readline().split()]
            init_pos_l.append([P,V])


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %.8f\n" % (case_no,
                                         solve_case(case_no, D, init_pos_l)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
