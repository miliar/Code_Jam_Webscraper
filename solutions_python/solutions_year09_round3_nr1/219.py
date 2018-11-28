def uniq(it):
    seen = set()
    for x in it:
        if x not in seen:
            yield x
            seen.add(x)

def guess(line, m, base):
    result = 0
    for c in line:
        result *= base
        result += m[c]
    return result

digits = [1,0] + range(2,62)
def solve(line):
    m = dict(zip(uniq(line), digits))
    base = len(m)
    if base == 1: base = 2
    return guess(line, m, base)

import sys; f=sys.stdin
next(f)
for i, line in enumerate(f,1):
    print 'Case #%d: %d' % (i, solve(line.strip()))
