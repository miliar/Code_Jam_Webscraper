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

    in_s  ="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    out_s ="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

    mapping_d = {}

    for i in range(len(in_s)):
        i_c = in_s[i]
        o_c = out_s[i]

        mapping_d[i_c] = o_c

    mapping_d["q"] = "z"

    all_letters = set([chr(i) for i in range(ord("a"), ord("z") +1)])

    missing = all_letters - set(mapping_d.values())
    mapping_d["z"] = missing.pop()

    for i in sorted(mapping_d.keys()):
        print i, '->', mapping_d[i]

    return mapping_d


def solve_case(case_no,  line , mapping_d  ):
    print "-------------- New case", case_no

    line_out = ""
    for c in line:
        line_out += mapping_d[c]

    return line_out


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    mapping_d = init()

    for case_no in range(1, nb_cases+1):

        line = fd.readline().rstrip()


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %s\n" % (case_no,
                                         solve_case(case_no, line, mapping_d)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
