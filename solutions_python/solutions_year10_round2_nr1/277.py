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


def get_subdirs(adir):
    ret_l = []
    adir_splitted = adir.split("/")
    for i in range(2, len(adir_splitted)+1):
            b = "/".join(adir_splitted[:i])
            ret_l.append(b)

    return ret_l

def solve_case(case_no,   N, M, dir_exist_l, dir_new_l   ):
    print "-------------- New case", case_no

    dir_exist_s = set(dir_exist_l)

    # put all
    print "------"
    for adir in dir_exist_l:
        for item in get_subdirs(adir):
            if item not in dir_exist_s:
                dir_exist_s.add(item)


    nb  = 0

    for ndir in dir_new_l:
        for item in get_subdirs(ndir):
            if item not in dir_exist_s:
                dir_exist_s.add(item)
                nb += 1

    return nb


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        N, M = [int(item) for item in fd.readline().split()]

        dir_exist_l = []
        dir_new_l = []
        for i in range(N):
            dir_exist_l.append(fd.readline().strip())
        for i in range(M):
            dir_new_l.append(fd.readline().strip())

        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, N, M, dir_exist_l, dir_new_l)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
