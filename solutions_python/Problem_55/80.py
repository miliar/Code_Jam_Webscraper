#!/usr/bin/env python

from sys import stdin, stdout

for x in range(1, int(stdin.readline()) + 1):
    (R, k, N) = map(int, str.split(stdin.readline()))
    gi = map(int, str.split(stdin.readline()))
    assert(len(gi) == N)
    
    # compute for each group i waiting in front of the line
    # - the money made EURi of the next ride
    # - the group NEXTi now waiting in front of the line
    (EURi, nexti) = ([], [])
    for i in xrange(N):
        EUR = 0
        left = k
        next = i
        while True:
            EUR += gi[next]
            left -= gi[next]
            next = (next + 1) % N
            if left < gi[next] or next == i:
                break
        EURi.append(EUR)
        nexti.append(next)

    # compute the result a la fast exponentiation
    EUR = 0
    next = 0
    while R > 0:
        # apply the current transition
        if (R % 2) == 1:
            EUR += EURi[next]
            next = nexti[next]
            R = R - 1
        # compute the squared transitions
        (EURi2, nexti2) = ([], [])
        for i in xrange(N):
            EURi2.append(EURi[i] + EURi[nexti[i]])
            nexti2.append(nexti[nexti[i]])
        (EURi, nexti) = (EURi2, nexti2)
        R = R // 2
    
    # output
    stdout.write('Case #%i: %i\n' % (x, EUR))

