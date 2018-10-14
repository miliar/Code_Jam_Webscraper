#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'duc_tin'

import re
from itertools import combinations_with_replacement, product


def monkey(keyboard, target, S):
    if not set(target) <= set(keyboard):
        return 0.0

    possibles = product(keyboard, repeat=S)
    total = 0
    match_no = []
    for stri in possibles:
        total += 1
        match_no.append(len(re.findall(r'(?=(%s))' % target, ''.join(stri))))

    return max(match_no) - float(sum(match_no))/total


T = int(raw_input())
for case in range(T):
    K, L, S = [int(x) for x in raw_input().split()]
    keyboard = raw_input()
    target = raw_input()
    res = monkey(keyboard, target, S)
    print 'Case #%s: %f' % (case + 1, res)

