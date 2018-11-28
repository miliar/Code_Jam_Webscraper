#!/usr/bin/python

"""
  Google Code Jam 2008
  philfifi@free.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

import psyco
psyco.full()

_debug = 0


def aire_triangle(x1, y1, x2, y2, x3, y3):
    """ return twice the area"""
    return abs( (x2 - x1) * (y3-y1) - (x3-x1)*(y2-y1) )

def solve_case(case_no, A, N, M    ):
    print "-------------- New case", case_no
    print "aire x2:", A

    for x1 in range(1):
        for x2 in range(x1, N+1):
            for x3 in range(x2, N+1):
                for y1 in range(1):
                    for y2 in range(0, M+1):
                        for y3 in range(0, M+1):
                            airex2 = aire_triangle(x1, y1, x2, y2, x3, y3)
                            if airex2 == A:
                                print airex2
                                return "%d %d %d %d %d %d" % (x1, y1, x2, y2, x3, y3)
                

    return "IMPOSSIBLE"
        
            
def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        N, M, A = [int(item) for item in fd.readline().split()]

    
        # Have read all stuff for this case:
        f_out.write( "Case #%d: %s\n" % (case_no,
                                         solve_case(case_no, A, N, M)
                                         )
                     )
        f_out.flush()

    f_out.close()
    
    for line in open(f_out_name):
        print line,

    

import sys
if __name__ == "__main__":
    main(sys.argv)
