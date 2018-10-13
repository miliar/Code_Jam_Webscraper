#!/usr/bin/python
# -*- coding: utf-8 -*-
## Problem B. Dancing With the Googlers (GCJ Qualification Round 2012)

def dancer(N, S, p, tab):
    sol = 0

    for total in tab:
        median = total/3.
        if (median >= p) or ((p-1) < median):
            ## victoire
            sol += 1
        elif (total < p):
            ## aucune chance
            pass
        elif (median <= (p-1)):
            if S > 0:
                ## on retire p au total et on regarde la nouvelle médiane
                m = (total-p) / 2 # forme : (a.5 ou a) => on prend a
                if m >= (p-2):
                    S -= 1 ## joker
                    sol += 1

    return sol

if __name__ == "__main__":
    T = int(raw_input()) ## nb of test cases

    for x in xrange(T):
        tab = map(int, raw_input().split())
        N, S, p, tab = tab[0], tab[1], tab[2], tab[3:]
        char = "Case #%d: %d" %(x+1, dancer(N, S, p, tab))
        print char
