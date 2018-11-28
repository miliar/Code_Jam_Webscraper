#!/usr/bin/python
import sys

# Standing Ovation

lines = [l.rstrip() for l in sys.stdin.readlines()]
for i in xrange(int(lines.pop(0))):
    s = [int(c) for c in lines[i].split(' ')[1]]
    invite, standing = 0, 0
    for k in xrange(len(s)):
        if k > standing:
            invite += k - standing
            standing += k - standing
        standing += s[k]
    print "Case #%u: %s" % (i + 1, invite)
