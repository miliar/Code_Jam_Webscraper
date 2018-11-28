#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 et

from __future__ import division

import sys



def run_testcase():
    bases = {}
    opposing = {}
    input_tokens = raw_input().strip().split()

    # How many base strings?
    C = int(input_tokens.pop(0))
    for i in range(C):
        s = input_tokens.pop(0)
        bases[s[0]+s[1]] = bases[s[1]+s[0]] = s[2]

    # How many opposing strings?
    D = int(input_tokens.pop(0))
    for i in range(D):
        s = input_tokens.pop(0)

        o = opposing.get(s[0], set())
        o.add(s[1])
        opposing[s[0]] = o;

        o = opposing.get(s[1], set())
        o.add(s[0])
        opposing[s[1]] = o;

    # How many characters being invoked?
    N = int(input_tokens.pop(0))
    spell = input_tokens.pop(0)

    # Element list
    el = []
    for c in spell:
        el.append(c)

        # Combining base elements
        if len(el) >= 2:
        #while len(el) >= 2:
            non_basic = bases.get(el[-1] + el[-2], None)
            if non_basic:
                el[-2:] = non_basic
        #    else:
        #        break

        # Opposing elements
        o = opposing.get(el[-1], None)
        if o:
            if o.intersection(el[:-1]):
                el = []

    return "[{0}]".format(
        ', '.join(x for x in el)
    )





max_testcases = int(raw_input())
for T in range(1, max_testcases+1):
    print "Case #{0}: {1}".format(T, run_testcase())
