#!/usr/bin/env python

import logging
LOGGER = logging.getLogger(__name__)

T = int(raw_input().strip())

class ImpossibleError(Exception):
    pass

def flip(S, K, n):
    LOGGER.debug("Flipping %s, with %d, at %d", S, K, n)
    if n + K > len(S):
        raise ImpossibleError
    for i in range(0, K):
        S[n+i] = not S[n+i]

def calc(S, K):
    count = 0
    try:
        for n in range(0, len(S)):
            if not S[n]:
                # We need to flip
                flip(S, K, n)
                count += 1
    except ImpossibleError:
        return 'IMPOSSIBLE'

    assert all(S)
    return count


for i in range(1, T+1):
    logging.basicConfig(level=logging.INFO)

    print ("Case #%d:" % i),
    S, K = raw_input().strip().split()
    S = [(x == '+') for x in S]
    K = int(K)
    print calc(S, K)
