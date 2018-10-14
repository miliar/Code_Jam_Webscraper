#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'duc_tin'


def check():
    invite = 0
    stand_up = int(si[0])
    for need in range(1, len(si)):
        if need <= stand_up:
            stand_up += si[need]
        else:
            invite_now = need - stand_up
            invite += invite_now
            stand_up += invite_now + si[need]
    return invite




T = int(raw_input())

for case in range(T):
    simax, si = raw_input().strip().split(' ')
    simax = int(simax)
    si = [int(x) for x in list(si)]
    res = check()
    print 'Case #%s: %d' % (case+1, res)