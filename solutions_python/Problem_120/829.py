import math
import codejam

for case in xrange(codejam.readint()):
    r, t = map(int, codejam.readstring().split())
    lines = 0
    last = 0
    i = 0
    while t > 0:
        current = (r + i) * (r + i)

        if i % 2 != 0:
            t -= (current - last)
            if t >= 0:
                lines += 1

        i += 1
        last = current

    print "Case #%d: %s" % (case + 1, lines)
