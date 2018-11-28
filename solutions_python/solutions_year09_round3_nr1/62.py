from __future__ import with_statement
import sys
import itertools

with open(sys.argv[1]) as f:
    num_cases = int(f.readline())

    for c in xrange(1, num_cases+1):
        text = f.readline().strip()

        digit = dict(( (a, 0) for a in set(text) ))
        seen = []
        d = 2
        for a in text:
            if a not in seen:
                seen.append(a)
                if len(seen) == 1:
                    digit[a] = 1
                elif len(seen) == 2:
                    digit[a] = 0
                else:
                    digit[a] = d
                    d += 1
        base = max(digit.values()) + 1
        number = [digit[a] for a in text]
        d = reduce(lambda x, y: base*x+y, number)

        print "Case #%d: %d" % (c, d)
