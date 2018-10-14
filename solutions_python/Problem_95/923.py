#!/usr/bin/env python

import sys

def read_words(handle):
    lines = [l.strip() for l in handle.readlines()]
    return lines[1:]

tr = {'y': 'a', 'e': 'o', 'q': 'z', 'z': 'q'}

for s1, s2 in zip(read_words(open('input')), read_words(open('output'))):
    for c1, c2 in zip(s1, s2):
        if not c1 in tr:
            tr[c1] = c2
        else:
            assert tr[c1] == c2

i = 1

for l in read_words(sys.stdin):
    print 'Case #{0}:'.format(i), ''.join([tr[c] for c in l])
    i += 1
