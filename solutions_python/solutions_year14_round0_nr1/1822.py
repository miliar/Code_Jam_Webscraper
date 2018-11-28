#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import sys
ifs = sys.stdin
ofs = sys.stdout

BAD = 'Bad magician!'
CHEAT = 'Volunteer cheated!'


def solve(r1, M1, r2, M2):
    #print r1, M1, r2, M2
    R1 = set(M1[r1 - 1])
    R2 = set(M2[r2 - 1])
    I = R1 & R2
    In = len(I)
    if In == 0:
        return CHEAT
    if In == 1:
        return I.pop()
    return BAD


def numbers_from_line(d=' '):
    return [int(s) for s in ifs.readline().strip().split(d)
            if len(s.strip()) > 0]


T = int(ifs.readline())
for t in range(1, T + 1):
    r1 = int(ifs.readline())
    M1 = [numbers_from_line() for _ in range(4)]
    r2 = int(ifs.readline())
    M2 = [numbers_from_line() for _ in range(4)]
    a = solve(r1, M1, r2, M2)
    ofs.write('Case #%d: %s\n' % (t, a))
