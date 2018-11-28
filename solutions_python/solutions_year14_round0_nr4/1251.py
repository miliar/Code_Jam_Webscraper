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

POS_WEIGHT=0
POS_WHO=1

def play_war(N, naomis_l, ken_l):
    assert N == len(naomis_l)
    if N == 0:
         return 0

    w_score = 0
    ns_l = sorted(naomis_l) # first is lighter
    ks_l = sorted(ken_l)

    index_n = N-1
    index_k = 0

    for i in range(N):
        w = ns_l[index_n]
        print "naomi plays[%d]"% index_n, w
        index_n -= 1
        if ks_l[-1] < w:
            # ken doesn't have any bigger
            w_score += 1
            print "ken plays@[%d] LOOSE" % 0, ks_l[0]
            del ks_l[0] # ken plays its lighter
            index_k = 0
            continue

        # ken choose one just heavier
        while index_k > 0:
            # go left
            if ks_l[index_k] > w:
                index_k -= 1
            else:
                break
        if ks_l[index_k] > w:
            print "ken plays[%d] WINS" % index_k, ks_l[index_k]
            del ks_l[index_k]

        else:
            while True:
                # go right
                if ks_l[index_k] > w:
                    break
                else:
                    index_k += 1

            print "ken plays*[%d] WINS" % (index_k), ks_l[index_k]
            del ks_l[index_k]
        index_k = max(0, index_k-1)

    return w_score



def solve_case(case_no, N, naomis_l, ken_l    ):
    print "-------------- New case", case_no

    NAOMI = 0
    KEN = 1

    ns_l = sorted(naomis_l) # first is lighter
    ks_l = sorted(ken_l)

    print "Naomi", ns_l
    print "Ken  ", ks_l

    glob_order = []  #tuple (weight, NAOMI/KEN, index_in? )

    index_in_n = 0
    index_in_k = 0

    for i in range(2*N):
        if index_in_n < N:
            n = ns_l[index_in_n]
        else:
            n = None
        if index_in_k < N:
            k = ks_l[index_in_k]
        else:
            k = None
        if n is None or (k is not None and k < n):
            glob_order.append((k, KEN, index_in_k))
            index_in_k += 1
        else:
            glob_order.append((n, NAOMI, index_in_n))
            index_in_n += 1

#    print glob_order

    print "------- Play war"
    w_score = play_war(N, naomis_l, ken_l)


    # Cheating
    print "------- Cheating !"
    dw_score = 0
    while N:
        if ns_l[0] < ks_l[0]:
            #Naomi has the lighter block
            print "DEL ken %s with naomi %s" % (ks_l[-1], ns_l[0])
            del ns_l[0]
            del ks_l[-1]
        else:
            # Smaller of naomi is bigger than ken's
            print "Naomi wins %s against %s" % (ns_l[0], ks_l[0])
            del ns_l[0]
            del ks_l[0]
            dw_score +=1
        N -= 1


    return "%d %d" % (dw_score, w_score)


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):
        N = int(fd.readline())
        naomis_l = [Decimal(item) for item in fd.readline().split()]
        ken_l = [Decimal(item) for item in fd.readline().split()]


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %s\n" % (case_no,
                                         solve_case(case_no, N, naomis_l, ken_l)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
