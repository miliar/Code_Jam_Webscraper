#!/usr/bin/env python3.2

import sys

mapping = str.maketrans('abcdefghijklmnopqrstuvwxyz',
                        'yhesocvxduiglbkrztnwjpfmaq')

def readline():
    return next(sys.stdin).strip()

def readvals(t):
    return map(t, readline().split())

ncases = int(readline())
for caseno in range(ncases):
    s = readline().translate(mapping)
    print('Case #{}: {}'.format(caseno + 1, s))
    sys.stdout.flush()
