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



def solve_case(case_no, L, t, N, ai    ):
    print "-------------- New case", case_no

    # how many times a ai is travelled ?
    print "nb_booster", L
    print "time to build", t

    print "nb_ai", len(ai)

    a, b = divmod(N, len(ai))

#    0-b : a+1 times
#    b:  : a times

    nb_times_ai = [a+1] * b + [a]*(len(ai) -b)

    index = 0
    index_ai_l = [] # tuple of (i, ai)
    for a in ai:
        index_ai_l.append( [index, a] )
        index += 1

#    print "index_ai_l", index_ai_l

    total_dist = 0
    for i in range(len(ai)):
        total_dist += ai[i] * nb_times_ai[i]

    print "total_dist", total_dist

    ai_sorted = sorted(index_ai_l, key=lambda x:x[1], reverse=True)
#    print "ai_sorted", ai_sorted




    total_dist_with_booster = 0

    total_dist_all_ai = sum(ai)
    print "total_dist_all_ai", total_dist_all_ai

    travel_time_max = total_dist * 2
    print "travel_time_max", travel_time_max

    if t < travel_time_max and L>0:

        # Start travel, get the first speed booster:
        travel_time = 0
        takeof_star_num = 0

        # we can do nb_full all ai :
        nb_full = max(0,
                      (t / total_dist_all_ai) -100 )
        nb_full = 0


        print "nb_full", nb_full

        for i in range(len(ai)):
            nb_times_ai[i] -= nb_full
        travel_time += 2*nb_full * total_dist_all_ai
        takeof_star_num += nb_full * len(ai)


        print "travel_time <= t", travel_time <= t

        while travel_time <= t:
            last_takeof_time = travel_time
            dist = ai[takeof_star_num % len(ai)]
            travel_time += 2*dist
            nb_times_ai[takeof_star_num % len(ai)] -= 1

            takeof_star_num += 1

    #        print "it's", travel_time, "hours"
    #        print "we landed on star", takeof_star_num
    #        print "after traveling", dist

    #    print "nb_times_ai after start", nb_times_ai











        dist_first_booster = dist - 0.5 * (t-last_takeof_time)
        print "dist_first_booster", dist_first_booster


        dist_nb_times_l = [(dist_first_booster, 1)] # tuple for (dist, nb_times)
        for i in range(len(ai)):
            dist = ai[i]
            nb_times = nb_times_ai[i]
            dist_nb_times_l.append( [dist, nb_times] )

    #    print "dist_nb_times_l", dist_nb_times_l

        dist_nb_times_sorted_l = sorted(dist_nb_times_l, key=lambda x:x[0])
    #    print "dist_nb_times_sorted_l", dist_nb_times_sorted_l

        while L > 0 and dist_nb_times_sorted_l:
            dist, nb_times = dist_nb_times_sorted_l.pop()

            m = min(nb_times, L)
            total_dist_with_booster += m * dist
            L -= m




    print "total_dist", total_dist
    print "total_dist_with_booster", total_dist_with_booster

    return (total_dist - total_dist_with_booster) * 2 + total_dist_with_booster


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        l = [int(item) for item in fd.readline().split()]
        L, t, N, C = l[0:4]
        ai = l[4:]
        assert len(ai) == C , "bad"


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, L, t, N, ai)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
