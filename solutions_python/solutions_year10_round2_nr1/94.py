#! /usr/bin/env python
#
#   A. File Fix-it
#

from __future__ import print_function

def add(d, path):
    if len(path) == 0:
        return 0
    sd = d.get(path[0])
    if sd is None:
        sd = {}
        d[path[0]] = sd
        return 1 + add(sd, path[1:])
    else:
        return add(sd, path[1:])

for case in xrange(1, int(raw_input())+1):
    nold, nnew = map(int, raw_input().split())
    root = {}
    for i in xrange(nold):
        add(root, raw_input()[1:].split('/'))
    ct = 0
    for i in xrange(nnew):
        ct += add(root, raw_input()[1:].split('/'))
    print("Case #{0}:".format(case), ct)
