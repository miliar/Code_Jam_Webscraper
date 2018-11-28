#!/usr/bin/env python

import logging
LOGGER = logging.getLogger(__name__)

T = int(raw_input().strip())

def tidy(N):
    return N == sorted(N)


def calc(N):
    if tidy(N):
        return N
    for i in range(len(N)-1, 0, -1):
        if N[i-1] > N[i]:
            N[i-1] = N[i-1] - 1
            for j in range(i, len(N)):
                N[j] = 9
    assert tidy(N)
    return N

for i in range(1, T+1):
    logging.basicConfig(level=logging.INFO)

    print ("Case #%d:" % i),
    N = [int(x) for x in raw_input().strip()]
    print int(''.join([str(x) for x in calc(N)]))
