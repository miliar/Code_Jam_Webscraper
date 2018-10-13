#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import *
import sys

bestAge=[]
bestAmount=0

if __name__ == "__main__":
    t = input()
    for caseIdx in xrange(1,t+1):
        index = input()-1
        row1 = set([map(int, raw_input().split()) for r in xrange(4)][index])
        index = input()-1
        row2 = set([map(int, raw_input().split()) for r in xrange(4)][index])

        intersect = row1.intersection(row2)
        if len(intersect) == 0:
            print "Case #%d: Volunteer cheated!" % caseIdx
        elif len(intersect) == 1:
            print "Case #%d: %d" % (caseIdx, list(intersect)[0])
        else:
            print "Case #%d: Bad magician!" % caseIdx

