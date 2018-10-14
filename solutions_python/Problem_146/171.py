#!/usr/bin/env python

import sys
import re
from itertools import permutations
from multiprocessing import Pool

def getl():
    return sys.stdin.readline().strip()

def train_norm(s):
    return re.sub(r'(.)\1+', r'\1', s)

def train_ok(s):
    train_normalized = train_norm(s)
    return len(set(train_normalized)) == len(train_normalized)

def solve(sets):
    c = 0
    for p in permutations(sets):
        p_s = ''.join(p)
        if train_ok(p_s):
            c += 1
    return c

T = int(getl())

cases = []

for i in range(T):
    x = i + 1

    N = int(getl())
    s = getl().strip()

    sets = s.split(' ')
    if len(sets) != N:
        raise Exception('inconsistent set count data')

    # optimization
    sets = map(train_norm, sets)
    cases.append(sets)

p = Pool(8)
r = p.map(solve, cases)

for (i, x) in enumerate(r):
    print('Case #%i: %s' % (i+1, x))


