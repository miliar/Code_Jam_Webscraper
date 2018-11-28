#!/usr/bin/env python

for nnn in xrange(1, int(raw_input())+1):
    print "Case #%d:" % (nnn),
    S, K = raw_input().split()
    K = int(K)
    flipped, count, impossible = 0, 0, False
    f = [0] * (len(S)-K+1)
    for i in xrange(len(S)):
        if i >= K:
            flipped ^= f[i-K]
        if (flipped and S[i] == '+') or (not flipped and S[i] == '-'):
            if i > len(S)-K:
                impossible = True
                break
            f[i] = 1
            flipped ^= 1
            count += 1
    print 'IMPOSSIBLE' if impossible else count

