#! /usr/bin/env python

from string import *

subst =  {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

n = input()
for i in xrange(1, n + 1):
    line = raw_input()
    line = list(line)
    m = len(line)
    for j in xrange(m):
        if line[j] in ascii_lowercase:
            line[j] = subst[line[j]]
    print "Case #%d: %s" % (i, "".join(line))
    

