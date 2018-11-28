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


def get_index_nb_people(k, groups_l, index_max, start_index=0):

#    print "k, gr:", k, groups_l

    remaining = k
    index = start_index
    while index <= index_max:
        if groups_l[index] <= remaining:
            # ok, take it
            remaining -= groups_l[index]
            index += 1
        else:
            # cannot fit
            break

#    print "ret:", index, k-remaining
    return index, k-remaining

def get_hint_for(start_index, N, dbl_queue_l, k, index_max):
#    print "get hint for start", start_index
    last_index = start_index
    total = 0
    nb_run = 0
    while last_index < N:
#        print "    index", last_index
        last_index, nb = get_index_nb_people(k, dbl_queue_l, 2*index_max, start_index=last_index)
        total += nb
#        print "     money", nb
        nb_run += 1

#    print "  next_index", last_index-N
#    print "  money", total
    return total, nb_run, last_index - N


def solve_case(case_no, R, k, N, groups_l    ):
  print "-------------- New case", case_no

  if R == 0:
        # Roller is off !
        return 0

  elif sum(groups_l) <= k:
        # everybody fit
        return R * sum(groups_l)

  else:
    # Analyse the queue
    dbl_queue_l = groups_l + groups_l + groups_l

    hint_d = {}
    #start_index -> total_nb_people, nb_run, new_start_index

    start_index = 0
    total_money = 0

    nb_run = 0
    index_max = len(groups_l)
    while nb_run < R:
        if start_index in hint_d:
            hint_total_nb_people, hint_nb_run, hint_new_start_index = hint_d[start_index]
#            print "hit !"
        else:
            hint_total_nb_people, hint_nb_run, hint_new_start_index = get_hint_for(start_index, N, dbl_queue_l, k, index_max)
            hint_d[start_index] = hint_total_nb_people, hint_nb_run, hint_new_start_index

        if hint_nb_run <= R-nb_run:
            # Ok, we can do it all:
            total_money += hint_total_nb_people
            nb_run += hint_nb_run
            start_index = hint_new_start_index
        else:
#            print "manual"
            # we cannot run this queue entierly:
            start_index, nb_people = get_index_nb_people(k, dbl_queue_l, index_max, start_index=start_index)
            total_money += nb_people
            nb_run += 1

#        print "nb_run=%5d, money=%5d" % (nb_run, total_money)

    return total_money





def solve_case_good(case_no, R, k, N, groups_l    ):
    print "-------------- New case", case_no

    if R == 0:
        # Roller is off !
        return 0

    elif sum(groups_l) <= k:
        # everybody fit
        return R * sum(groups_l)

    else:
        #double the queue now:
        total_money = 0
        for _ in range(1, R+1):

            # Calculate a run
#            up_to_index, this_run_nb_people = get_index_nb_people(k, groups_l)



            remaining = k
            up_to_index = 0
            while True:
                this_group = groups_l[up_to_index]
                if this_group <= remaining:
                    # ok, take it
                    remaining -= this_group
                    up_to_index += 1
                else:
                    # cannot fit
                    break

            this_run_nb_people = k-remaining

            total_money += this_run_nb_people
            groups_l = groups_l[up_to_index:] + groups_l[:up_to_index]

#            print "nb_run=%5d, money=%5d" % (_, total_money)

        return total_money

def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        R, k, N = [int(item) for item in fd.readline().split()]
        groups_l = [int(item) for item in fd.readline().split()]


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, R, k, N, groups_l)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
