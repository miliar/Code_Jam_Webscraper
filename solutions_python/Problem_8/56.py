import sys

def find_primes(n):
    """Generate a list of the prime numbers [2, 3, ... m] where
    m is the largest prime <= n."""
    n = n + 1
    sieve = range(n)
    sieve[:2] = [0, 0]
    for i in xrange(2, int(n**0.5)+1):
        if sieve[i]:
            for j in xrange(i**2, n, i):
                sieve[j] = 0
    # Filter out the composites, which have been replaced by 0's
    return [p for p in sieve if p]

n_cases = input()
for _i in xrange(n_cases):
    line = sys.stdin.readline().rstrip()
    A, B, P = [int(n) for n in line.split(' ')]
    L = []
    for i in xrange(A, B + 1):
        L.append(i)
#    print L

    sets = set()
    for p in (p for p in find_primes(B) if p >= P):
        s = set()
        start = (A / p) * p
        if A % p:
            start += p
#        print p, 'start ', start
        for n in xrange(start, B + 1, p):
            s.add(n)
#        print 'for ', p, ', ', s
        if s:
            sets.add(frozenset(s))
        
    unfactored = []
    for n in xrange(A, B + 1):
        for s in sets:
            if n in s:
                break
        else:
            unfactored.append(n)
#    print 'unfactored', unfactored

    while True:
        unioned = False
#        print sets
        for s in sets:
            for s2 in sets:
                if s2 is s:
                    continue
                if s.intersection(s2):
                    sets.remove(s)
                    sets.remove(s2)
                    s3 = s.union(s2)
                    sets.add(frozenset(s3))
#                    assert len(s) < len(s3), '%s, %s, %s' % (s, s2, s3)
                    unioned = True
                    break
            if unioned:
                break
        if not unioned:
            break
#    print sets

#    print L
    print 'Case #%d: %s' % (_i + 1, len(sets) + len(unfactored))
