import itertools
import sys

# Round 1B - Problem A

i, result = 0, ""
lines = [l.rstrip() for l in sys.stdin.readlines()]
lines.pop(0)
while lines:
    i += 1
    n = int(lines.pop(0))
    l = lines[:n]
    del lines[:n]
    r = ["".join([k for k, g in itertools.groupby(x)]) for x in l]
    if len(set(r)) > 1:
        result = "Fegla Won"
    else:
        v = [[list(g) for k, g in itertools.groupby(x)] for x in l]
        counts = [[len(c) for c in x] for x in v]
        target = [sum(c)/len(c) for c in zip(*counts)]
        moves = sum([sum([abs(num[x]-target[x]) for x in xrange(len(target))]) for num in counts])
        result = str(moves)
    print "Case #%u: %s" % (i, result)

