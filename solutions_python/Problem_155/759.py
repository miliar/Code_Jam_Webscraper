#!/usr/bin/env python
import math, sys;
lines = [line for line in sys.stdin];
for T, line in enumerate(lines[1:]):
    S = map(int, line.split(' ')[1].strip());
    standing = 0;
    brought = 0;
    for i, s in enumerate(S):
        if (standing >= i): standing += s;
        else:
            additional = i - standing;
            brought += additional;
            standing += additional + s;
    print "Case #%i: %i" % (T + 1, brought);
