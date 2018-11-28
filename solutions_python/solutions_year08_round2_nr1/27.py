#!/usr/bin/env python

from math import sqrt
from decimal import *
getcontext().prec = 100

import psyco
psyco.full()

_debug = 0


def get_tree_coord(n, A, B, C, D, x0, y0, M):
    ret_l = []

    X=x0
    Y=y0
    ret_l.append((X,Y))

    for i in range(1,n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M

        ret_l.append((X,Y))

    return ret_l


def get_center(c1, c2, c3):
    c_x_3 = (c1[0] + c2[0] + c3[0])
    c_y_3 = (c1[1] + c2[1] + c3[1])

    

    return ( c_x_3 % 3 == 0 and
             c_y_3 % 3 == 0 )
             

def solve_case(case_no, n, A, B, C, D, x0, y0, M    ):
    print "-------------- New case", case_no
    print n, 'trees'

    all_tree_coord = get_tree_coord(n, A, B, C, D, x0, y0, M)

    nb_valid_triangles = 0
    for c1 in all_tree_coord:
        for c2 in all_tree_coord:
            for c3 in all_tree_coord:

                if (c1 == c2 or
                    c1 == c3 or
                    c2 == c3):
                    # not distinct vertexes
                    continue

                if get_center(c1, c2, c3):
                    nb_valid_triangles += 1

    
    return nb_valid_triangles /6
        
            
def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        n, A, B, C, D, x0, y0, M = [int(item) for item in fd.readline().split()]

    
        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, n, A, B, C, D, x0, y0, M)
                                         )
                     )
        f_out.flush()

    f_out.close()
    
    for line in open(f_out_name):
        print line,

    

import sys
if __name__ == "__main__":
    main(sys.argv)
