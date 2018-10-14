import fractions
import sys

def solve(l):
    ref = l[0]
    diffs = [abs(ref-i) for i in l[1:]]
    gcd = reduce(lambda x,y:fractions.gcd(x,y), diffs)
    m = ref % gcd
    if m == 0:
        return 0
    return gcd - m

input = sys.stdin.read().splitlines()[1:]
for pb, line in enumerate(input):
    events = map(int, line.split()[1:])
    result = solve(events)

    print "Case #%d: %d" % (pb+1, result)

