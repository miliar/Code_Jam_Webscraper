#!/usr/bin/env python
import fileinput
from collections import defaultdict

incoming = fileinput.input()

num_cases = int(incoming.next())

def get_row_set():
    """Takes a row pick and 4 rows and returns set of #s from picked row"""
    pick = int(incoming.next())
    for skip in range(1, pick):
        incoming.next()
    numbers = set(incoming.next().split())
    for skip in range(pick, 4):
        incoming.next()
    return numbers

for case in xrange(1, num_cases+1):
    options = get_row_set() & get_row_set()
    if not options:
        print "Case #%d: Volunteer cheated!" % case
    elif len(options) > 1:
        print "Case #%d: Bad magician!" % case
    else:
        print "Case #%d: %s" % (case, list(options)[0])
