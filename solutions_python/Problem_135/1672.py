#!/usr/bin/env python
#-*- coding: utf-8 -*-

T = int (raw_input ())
for t in range (1, T + 1):
    S1, S2 = set (), set ()
    row = int (raw_input ())
    for i in range (1, 4 + 1):
        l = [int (x) for x in raw_input ().split ()]
        [S1.add (x) for x in l if i == row]
    row = int (raw_input ())
    for i in range (1, 4 + 1):
        l = [int (x) for x in raw_input ().split ()]
        [S2.add (x) for x in l if i == row]
    ret = len (S1.intersection (S2))
    if ret == 1: print "Case #{0}: {1}".format (t, S1.intersection (S2).pop ())
    elif ret > 1: print "Case #{0}: Bad magician!".format (t)
    else: print "Case #{0}: Volunteer cheated!".format (t)
