#!/usr/bin/env python 
######################################################################
## Filename:    roller.py
## Version:     $Revision: 1.0 $
## Description: 
## Creator:     Rui Pereira <rui.pereira@in2p3.fr>
## Created:     08-05-2010 15:39:54
## Modified:    Time-stamp: <2010-05-08 16:01:24 rui>
## CVS info:    $Id: roller.py, v 1.0 08-05-2010 15:39:54 pereira Exp $
######################################################################

import sys
import numpy as N

class Roller:
    def __init__(self, R, k, g):
        self.R, self.k, self.queue = R, k, g
        self.profit = 0

    def fill(self):
        w = self.queue.cumsum() <= self.k
        self.profit += self.queue[w].sum()
        self.queue = N.concatenate((self.queue[~w], self.queue[w]))

    def run(self):
        for i in range(self.R):
            self.fill()

def parse_input(filename):
    rollers = []
    inputs = open(filename).readlines()[1:]
    for i,j in zip(inputs[::2], inputs[1::2]):
        tmp = map(int, i.split()[:2])
        rollers.append(Roller(tmp[0], tmp[1], N.array(map(int, j.split()))))
    return rollers

if __name__ == "__main__":

    out = open('roller.out', 'w')
    rollers = parse_input(sys.argv[1])
    for i,roller in enumerate(rollers):
        roller.run()
        print >> out, 'Case #%i: %i' % (i+1, roller.profit)
    out.close()
