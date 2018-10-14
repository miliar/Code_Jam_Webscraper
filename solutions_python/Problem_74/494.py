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



def solve_case(case_no, seq_l    ):
    print "-------------- New case", case_no

    time = 0
    print seq_l
    pos_d = { 'O': 1,
              'B': 1}

    while seq_l:
        next_bot = seq_l[0]
        next_button = int(seq_l[1])

        other_bot = next_bot == "O" and 'B' or 'O'
        try:
            other_button = int(seq_l[seq_l.index(other_bot) +1])
        except ValueError:
            other_button = None

#        print "---- at time", time
#        print "pos: ", pos_d
#        print "next ", next_bot, next_button,
#        print "            other", other_bot, other_button

        if pos_d[next_bot] == next_button:
            seq_l = seq_l[2:]
#            print "--> press !"
        elif pos_d[next_bot] < next_button:
            pos_d[next_bot] += 1
        else:
            pos_d[next_bot] -= 1

#        print 'pos_other', pos_d[other_bot], "target", other_button
        if pos_d[other_bot] > other_button:
            pos_d[other_bot] -= 1
        elif pos_d[other_bot] < other_button:
            pos_d[other_bot] += 1

        time += 1

    return time


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, fd.readline().split()[1:])
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
