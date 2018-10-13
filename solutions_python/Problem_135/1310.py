#!/usr/bin/python2

"""
  Google Code Jam 2014
  Philfifi  --  http://www.pluc.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

#import psyco
#psyco.full()

_debug = 0



def solve_case(case_no, t1, ans1, t2, ans2    ):
    print "-------------- New case", case_no

    r1 = t1[ans1-1]
    r2 = t2[ans2-1]

    s = r1.intersection(r2)
    if len(s) == 1:
        return s.pop()
    elif len(s) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        ans1 = int(fd.readline())
        t1 = []
        for i in range(4):
            t1.append(set([int(item) for item in fd.readline().split()]))
        ans2 = int(fd.readline())
        t2 = []
        for i in range(4):
            t2.append(set([int(item) for item in fd.readline().split()]))


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %s\n" % (case_no,
                                         solve_case(case_no, t1, ans1, t2, ans2)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
