#!/usr/bin/env python

from math import sqrt
from decimal import *
getcontext().prec = 100

import psyco
psyco.full()

_debug = 0

def sort_deck_index(c1, c2):
    if (c1[1] > c2[1]):
        return 1
    elif (c1[1] < c2[1]):
        return -1
    else:
        return 0


def get_perfect_deck(K):
    deck_l = []
    deck_out = []
    for i in range(K):
        deck_l.append( [None, i] )  #List of (value of card, index at origin)

    


    for i in range(1,K+1):

        if _debug:
            print "before", deck_l
        switch = (i-1) % (len(deck_l))
        if True:
            deck_l = deck_l[switch:] + deck_l[:switch]
        else:
            for nb_reveal in range(i-1):
                reveal = deck_l.pop(0)
                deck_l.append(reveal)
        if _debug:
            print "after ", deck_l


        card_good = deck_l[0]
        card_good[0] = i
        deck_l.pop(0)
        
        deck_out.append(card_good)

        if _debug:
            print "deck for", i, deck_l

    deck_out.sort(sort_deck_index)

    return deck_out
    

def solve_case(case_no, K, di_l    ):
    print "-------------- New case", case_no
    print K, "cards"

    perfect_deck =  get_perfect_deck(K)

    ret_l = []
    for di in di_l:
        ret_l.append(str(perfect_deck[di-1][0]))
    
    return " ".join(ret_l)
        
            
def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        K = int(fd.readline())
        

        di = [int(item) for item in fd.readline().split()]
        nb_di = di[0]
        di = di[1:]

        assert nb_di == len(di), "Wrong !"
    
        # Have read all stuff for this case:
        f_out.write( "Case #%d: %s\n" % (case_no,
                                         solve_case(case_no, K, di)
                                         )
                     )
        f_out.flush()

    f_out.close()
    
    for line in open(f_out_name):
        print line,

    

import sys
if __name__ == "__main__":
    main(sys.argv)
