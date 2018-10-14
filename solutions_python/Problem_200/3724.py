#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division
import numpy as np
""" Qualification round. """

# NOTE: Oversized Pancake Flipper
def f_A(*args):
    S = str(args[0])
    K = int(args[1])

    S = np.array([pancake == '+' for pancake in S], dtype=np.bool)

    if all(S):
        return 0

    ps_visited = set()
    ps_tovisit = [S]
    step = 0
    while ps_tovisit:
        ps_next = []
        for ps in ps_tovisit:
            if all(ps):
                return step
            ps_tuple = tuple(ps)
            if ps_tuple not in ps_visited:
                ps_visited.add(ps_tuple)
                for i in xrange(len(ps)-K+1):
                    if not all(ps[i:i+K]):
                        ps_tmp = np.array(ps)
                        ps_tmp[i:i+K] = np.invert(ps_tmp[i:i+K])
                        ps_next.append(ps_tmp)
        step += 1
        ps_tovisit = ps_next
    return 'IMPOSSIBLE'


# NOTE: Tidy Numbers
def f_B(*args):
    n = int(args[0])
    while 1:
        s = str(n)
        if len(s) == 1:
            return n
        i = 0
        j = 1
        while j < len(s) and s[i] <= s[j]:
            i += 1
            j += 1
        if j == len(s):
            return n
        else:
            n = int(s[:j])*(10**(len(s)-j)) - 1
        if s == ''.join(sorted(s)):
            return n
    return n



# NOTE: Bathroom Stalls
def f_C(*args):
    return None

# NOTE: Fashion Show
def f_D(*args):
    return None


# f = f_A
f = f_B
#f = f_C
#f = f_D

t = int(raw_input())
for i in xrange(1, t + 1):
  args = [_ for _ in raw_input().split(" ")]
  print "Case #{}: {}".format(i, f(*args))
