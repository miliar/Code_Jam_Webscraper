#!/usr/bin/python

from __future__ import division
from gcj import *

# boolean flags, reachable via OPTS.flagname. Space separated in string
FLAGS = ''

def case():
    D, N = ints()
    h = []
    for i in range(N):
        K, S = ints()
        h.append((K, S))
    latest = max((D-k)/s for k,s in h)
    return '%f' % (D/latest)

if __name__ == '__main__':
    main()
