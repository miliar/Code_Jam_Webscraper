#!/usr/bin/python

lines = file('C-large.in.txt').read().splitlines()[1:]

for i in range(0, len(lines), 2):
    bags = map(int, lines[i+1].split())
    reduced = reduce(lambda x, y: x ^ y, bags)

    if reduced == 0:
        print "Case #%d: %d" % (i / 2 + 1, sum(bags) - min(bags))
    else:
        print "Case #%d: NO" % (i / 2 + 1)

