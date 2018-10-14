#!/usr/bin/env python

# No need to interpret as numbers, actually consider lists of digits
# [1,2,3] => 
#            [2,3] [1]
#            [3] [1,2]
# n = 3  => at most 2=(n-1) possibilities
#
# Complexity for N = A-B:
#   N*log(N)

def to_decimal(l):
    x = 0
    for e in l:
        x = 10*x+e
    return x

def from_decimal(n):
    return list(map(int, str(n)))

def uniq(l):
    ll = []
    for e in l:
        if e not in ll:
            ll.append(e)
    return ll

def possible_separations(n):
    l = from_decimal(n)
    return [to_decimal(k) for k in uniq([l[i:]+ l[:i] for i in range(1,len(l))]) if k > l]

def repeating_pairs(l, A, B):
    return [x for x in possible_separations(l) if A <= x <= B]

def n_repeating_pairs_between(A,B):
    n_pairs = 0
    for e in xrange(A,B+1):
        for f in repeating_pairs(e, A, B):
            n_pairs += 1
    return n_pairs

def parse(s):
    lines = s.splitlines()[1:]
    return [(int(a), int(b)) for a,b in map(str.split, lines)]

if '__main__' == __name__:
    import sys
    with open(sys.argv[1]) as f:
        cases = parse(f.read())
    for i,t in enumerate(cases):
        A,B = t
        print "Case #{}: {}".format(i+1, n_repeating_pairs_between(A,B))
