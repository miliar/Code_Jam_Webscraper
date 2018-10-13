import sys
import operator
f = sys.stdin

t = int(f.next())
for case in xrange(1, t+1):
    n = int(f.next())
    l = map(int, f.next().split())
    x = reduce(operator.xor, l, 0)
    if x == 0:
        result = sum(l) - min(l)
    else:
        result = "NO"
    print "Case #%d: %s" % (case, result)
