#!/usr/bin/env python

import sys

def extra_aud(ses):
    standing = 0
    extra = 0
    for i, s in enumerate(ses):
        s = int(s)
        if standing < i:
            extra += i - standing
            standing += i - standing
        standing += s
    return extra

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        t = int(f.readline())
        for i, line in enumerate(f):
            smax, ses = line.split()
            print("Case #{0}: {1}".format(i+1, extra_aud(ses)))
