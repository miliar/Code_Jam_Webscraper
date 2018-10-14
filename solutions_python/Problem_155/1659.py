#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# pylint: disable=invalid-name,missing-docstring,bad-builtin
from sys import stdin

def main():
    dstream = iter(stdin.read().split())
    for case in xrange(int(next(dstream))):
        _, aud = int(next(dstream)) + 1, map(int, next(dstream))
        curaud = 0
        invites = 0
        for i, x in enumerate(aud):
            if curaud < i and x:
                invites += i - curaud
                curaud += i - curaud
            curaud += x
        print "Case #{}: {}".format(case + 1, invites)

main()
