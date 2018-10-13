#!/usr/bin/env python
######################################################################
## Filename:    snapper.py
## Version:     $Revision: 1.0 $
## Description:
## Creator:     Rui Pereira <rui.pereira@in2p3.fr>
## Created:     08-05-2010 12:57:21
## Modified:    Time-stamp: <2010-05-08 14:08:27 rui>
## CVS info:    $Id: snapper.py, v 1.0 08-05-2010 12:57:21 pereira Exp $
######################################################################

import sys

class Snapper:
    def __init__(self, inp=False):
        self.input = inp
        self.status = False
        self.output = False

    def snap(self):
        if self.input:
            self.status = not self.status

    def refresh(self, inp):
        self.input = inp
        self.output = self.input and self.status

def parse_input(filename):
    cases = []
    for l in open(filename):
        cases.append(l.split())
    cases = cases[1:]
    return cases

def snapall(snappers):
    for s in snappers:
        s.snap()
    #first snapper is always on
    snappers[0].refresh(True)
    for i in range(len(snappers)-1):
        snappers[i+1].refresh(snappers[i].output)
    return snappers

if __name__ == "__main__":
    cases = parse_input(sys.argv[1])
    out = open('snapper.out', 'w')
    for i,case in enumerate(cases):
        N, K = case
        snappers = [Snapper(True)] + [Snapper(False) for s in range(int(N)-1)]
        for k in range(int(K)):
            snappers = snapall(snappers)
        print >> out, 'Case #%i: %s' % (i+1, 'ON' if snappers[-1].output else 'OFF')
