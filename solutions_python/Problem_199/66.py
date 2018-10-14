#!/usr/bin/python

from __future__ import division
from gcj import *

# boolean flags, reachable via OPTS.flagname. Space separated in string
FLAGS = ''

def case():
    S, K = line().split()
    K = int(K)
    cur = '+'
    flips = 0
    rev = dict()
    for i in range(len(S)-K+1):
        if i in rev:
            cur = '-' if cur == '+' else '+'
        if S[i] == cur: continue
        flips += 1
        cur = '-' if cur == '+' else '+'
        rev[i+K] = 1
    for i in range(len(S)-K+1, len(S)):
        if i in rev:
            cur = '-' if cur == '+' else '+'
        if S[i] != cur:
            return 'IMPOSSIBLE'
    return flips


if __name__ == '__main__':
    main()
