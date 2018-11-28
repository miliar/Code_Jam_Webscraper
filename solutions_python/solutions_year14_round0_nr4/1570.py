#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import *
import sys

def points( inputTolder, inputReceiver ):
    tolder = sorted(inputTolder)
    receiver = sorted(inputReceiver)
    tolder_points = 0
    receiver_points = 0
    idx_receiver = 0
    while idx_receiver < len(receiver):
        while( idx_receiver < len(receiver) and tolder[0] >= receiver[idx_receiver] ):
            idx_receiver += 1
        if( idx_receiver < len(receiver) ):
            receiver_points += 1
            del tolder[0]
            del receiver[idx_receiver]

    for idx in xrange(len(tolder)):
        if( tolder[idx] > receiver[len(tolder)-idx-1] ):
            tolder_points += 1

    return [tolder_points, receiver_points]

if __name__ == "__main__":
    t = input()
    for caseIdx in xrange(1,t+1):
        n = input()
        naomi = map(float, raw_input().split())
        ken = map(float, raw_input().split())

        naomi = sorted(naomi)
        ken = sorted(ken)

        deceitful_game = points(ken, naomi)
        war_game = points(naomi, ken)

        print "Case #%d: %d %d" % (caseIdx, deceitful_game[1], war_game[0])
