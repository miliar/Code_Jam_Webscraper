#!/usr/bin/python

import io
import sys

f = open("input.txt")

cases = int(f.readline())

for c in range(cases):
    n_str, participants = f.readline().split(" ")
    n = int(n_str)
    friends = 0
    # if participants[0] == '0':
    #    friends = 1
    standing = friends
    shyness = 0
    for p in participants.strip():
        np = int(p)
        if np != 0 and standing < shyness:
            friends += shyness - standing
            standing += friends
        standing += np
        shyness += 1

    print "Case #%d: %d" % (c + 1, friends)
    sys.stdout.flush()

