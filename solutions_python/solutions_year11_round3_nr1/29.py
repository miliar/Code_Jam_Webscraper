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



def solve_case(case_no, R, C, tile_l    ):
    print "-------------- New case", case_no

    print tile_l

    ret_l = [""]
    imp = "\nImpossible"

    for r in range(R-1):
        for c in range(C-1):
            t = tile_l[r][c]
            ta = tile_l[r][c+1]
            tb = tile_l[r+1][c]
            tc = tile_l[r+1][c+1]
            if t == "#":
                if ta == "#" and tb == "#" and tc == "#":
                    tile_l[r][c] = "/"
                    tile_l[r][c+1] = "\\"
                    tile_l[r+1][c] = "\\"
                    tile_l[r+1][c+1] = "/"
                else:
                    return imp


    for r in range(R):
        ret_l.append("".join(tile_l[r]))

    ret = "\n".join(ret_l)
    if "#" in ret:
        return imp
    else:
        return ret



def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        R, C = [int(item) for item in fd.readline().split()]

        tile_l = [None] * R
        for r in range(R):
            tile_l[r] = [ c for c in fd.readline().strip()]

        # Have read all stuff for this case:
        f_out.write( "Case #%d: %s\n" % (case_no,
                                         solve_case(case_no, R, C, tile_l)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
