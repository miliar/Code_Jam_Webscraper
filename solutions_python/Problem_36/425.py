#!/usr/bin/python

"""
  Google Code Jam 2009
  philfifi@free.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

import psyco
psyco.full()

_debug = 0

welcome = "welcome to code jam"

def solve_case(case_no, str_case     ):
    print "-------------- New case", case_no

    how_many = 0


    how_many_up_to_index_l = [0] * (len(welcome) +1)
    how_many_up_to_index_l[0] = 1

    for index_case in range(len(str_case)):
        letter_case = str_case[index_case]

        for index_welcome in range(len(welcome)):
            letter_welcome = welcome[index_welcome]

            if (letter_case == letter_welcome):
                how_many_up_to_index_l[index_welcome+1] += how_many_up_to_index_l[index_welcome]



    print how_many_up_to_index_l

    return (how_many_up_to_index_l[len(welcome)] % 1000)


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        str_to_test = fd.readline()


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %04d\n" % (case_no,
                                           solve_case(case_no,str_to_test )
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
