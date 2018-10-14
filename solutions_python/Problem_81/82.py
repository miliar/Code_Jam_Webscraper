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


def nb_win(l):
    res = 0
    for i in l:
        if i:
            res += 1
    return float(res)

def nb_match(l):
    res = 0
    for i in l:
        if i is not None:
            res += 1
    return float(res)

def solve_case(case_no, tbl    ):
    print "-------------- New case", case_no

    data_l = [None] * len(tbl)
    for i in range(len(tbl)):
        data_l[i] = [None] * len(tbl)

    nb_team = len(tbl)

    for i in range(len(tbl)):
        for j in range(len(tbl)):
            c = tbl[i][j]
            if c == ".":
                pass
            else:
                res = bool(int(c))
                data_l[i][j] = res

    opponents_l = [None] * len(tbl)
    for i in range(len(tbl)):
        ret = []
        for j in range(len(tbl)):
            if data_l[i][j] is not None:
                ret.append(j)
        opponents_l[i] = ret



    nb_win_l = [0] * len(tbl)
    wp_l = [0] * nb_team
    for i in range(len(tbl)):
        nb_win_l[i] = nb_win(data_l[i])
        wp_l[i] = nb_win_l[i] / len(opponents_l[i])

    nb_win_excluding = [None] * nb_team
    wp_excl_l = [0] * nb_team
    for i in range(len(tbl)):
        nb_win_excluding[i] = [None] * len(tbl)
        wp_excl_l[i] = [None] * len(tbl)
        for j in range(len(tbl)):
            d = data_l[i][:j] + data_l[i][j+1:]
            nb_win_excluding[i][j] = nb_win(d)
#            print "team", i, "win", nb_win(d), "excluding match with", j
#            print "        ", d
            wp_excl_l[i][j] = nb_win(d) / nb_match(d)


    owp_l = [0] * nb_team
    for i in range(len(tbl)):
        owp = 0.
        for op in opponents_l[i]:
            owp += wp_excl_l[op][i]

        owp_l[i] = owp / len(opponents_l[i])

    oowp_l = [0] * nb_team
    for i in range(len(tbl)):
        oowp = 0.
        for op in opponents_l[i]:
            oowp += owp_l[op]

        oowp_l[i] = oowp / len(opponents_l[i])

#    for i in range(nb_team):
#        print "team", i
#        print "  wp ", wp_l[i]
#        print "  opp:", opponents_l[i]
#        for op in opponents_l[i]:
#            print "  wp of opp %d (excluding %d): " % (op, i), wp_excl_l[op][i]
#        print "  owp", owp_l[i]

#        oowp = 0.
#        for op in opponents_l[i]:
#            print "  owp of opp %d : " % (op), owp_l[op]

#        print "  oowp", oowp_l[i]


    # -----------
    rpi_l = [0] * len(tbl)

    for i in range(len(tbl)):
        opp_l = opponents_l[i]
        nb_opp = len(opp_l)
        rpi = 0.25 * wp_l[i] + \
              0.50 * owp_l[i] + \
              0.25 * oowp_l[i]


        rpi_l[i] = rpi


    return rpi_l


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        nb_team = int(fd.readline())
        tbl = [None] * nb_team
        for i in range(nb_team):
            tbl[i] = fd.readline().strip()


        # Have read all stuff for this case:
        f_out.write( "Case #%d:\n" % (case_no))
        for rpi in solve_case(case_no, tbl):
            f_out.write("%.12f\n" % rpi)
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
