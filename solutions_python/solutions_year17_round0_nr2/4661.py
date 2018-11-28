#!/usr/local/bin/python

import sys

def is_tidy(n):
    s = str(n)
    if len(s) == 1:
        return True

    last = s[0]
    s = s[1:]

    for d in s:
        if d < last:
            return False

        last = d

    return True


with open(sys.argv[1]) as f:
    f.readline()
    i = 1
    for line in f:
        n = int(line.strip())
        while not is_tidy(n):
            n = n - 1

        print('Case #{}: {}'.format(i, n))
        i = i + 1

