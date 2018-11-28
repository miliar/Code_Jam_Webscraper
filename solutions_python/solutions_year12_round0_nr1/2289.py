#!/usr/bin/env python

"""
ejp mysljylc kd kxveddknmc re jsicpdrysi
our language is impossible to understand

rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
there are twenty six factorial possibilities

de kr kd eoya kw aej tysr re ujdr lkgc jv
so it is okay if you want to just give up
"""

import sys

regular    = "abcdefghijklmnopqrstuvwxyz "
googlerese = "ynficwlbkuomxsevzpdrjgthaq "

def decipher(subject):
    string = ""

    for c in subject:
        string += regular[googlerese.find(c)]

    return string

if __name__ == "__main__":
    lines = int(sys.stdin.readline())

    for i in xrange(lines):
        line = sys.stdin.readline()

        print "Case #%d: %s" % (i + 1, decipher(line))
