#!/usr/bin/python2

"""
  Google Code Jam 2011
  Philfifi  --  http://www.pluc.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100


_debug = 0



def solve_case(case_no, combine_l, oppose_l, invoke    ):
    print "-------------- New case", case_no

    print combine_l, oppose_l, invoke

    comb_d = {}
    for A, B, C in combine_l:
        comb_d[A+B] = [C]
        comb_d[B+A] = [C]

    opp_d = {}
    for A,B in oppose_l:
        opp_d[A] = opp_d.get(A, []) + [B]
        opp_d[B] = opp_d.get(B, []) + [A]

    out_l = [invoke[0]]
    invoke = invoke[1:]


#    print "invoke", out_l[0]
#    print "new ->", out_l

    for c in invoke:
#        print "invoke", c
        combine_or_oppose = False
        if len(out_l) >= 1:
            test = out_l[-1] + c

            if test in comb_d:
                out_l = out_l[:-1] + comb_d[test]
#                print "combine !"
                combine_or_oppose = True

            elif c in opp_d:
#                print "Might oppose with", opp_d[c]
                for other in opp_d[c]:
#                    print "test if", other, "in the list", out_l
                    if other in out_l:
                        out_l = []
#                        print "Oppose !"
                        combine_or_oppose = True
                        break

        if not combine_or_oppose:
#            print "NO action"
            out_l.append(c)

#        print "  new ->", out_l


    return "[" + ", ".join(out_l) + "]"


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        items = fd.readline().split()

        C = int(items.pop(0))
        combine_l = items[:C]; items = items[C:]

        D = int(items.pop(0))
        oppose_l = items[:D]; items = items[D:]

        N = items.pop(0)
        invoke = items.pop(0)

        assert len(items) == 0, "What %d" % len(items)

        # Have read all stuff for this case:
        f_out.write( "Case #%d: %s\n" % (case_no,
                                         solve_case(case_no, combine_l, oppose_l, invoke)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
