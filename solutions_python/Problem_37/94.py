MAX_ITER=99999
import sys; sys.setrecursionlimit(MAX_ITER)

def digits(n, base):
    while n:
        digit=n%base
        yield digit
        n=n/base

def ishappy(n, base, iter, trail):
    if n in trail:
        return False
    if not n:
        return False
    if iter > MAX_ITER:
        return False

    s=sum(d*d for d in digits(n, base))
    #print '-', iter, n, s
    if s==1:
        return True
    else:
        trail.add(n)
        return ishappy(s, base, iter+1, trail)

def solve(bases):
    for n in xrange(2, 99999):
        for pred in [ishappy(n, base, 0, set()) for base in bases]:
            if not pred:
                break
        else:
            return n

import sys
f=sys.stdin
next(f)
for i, line in enumerate(f):
    print 'Case #%d: %d' % (i+1, solve([int(base) for base in line.split()]))
    
