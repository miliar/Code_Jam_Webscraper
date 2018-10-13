#!/usr/bin/env python

mtab = {}
mtab[('1', '1')] = ('1', 1)
mtab[('1', 'i')] = ('i', 1)
mtab[('1', 'j')] = ('j', 1)
mtab[('1', 'k')] = ('k', 1)

mtab[('i', '1')] = ('i', 1)
mtab[('i', 'i')] = ('1', -1)
mtab[('i', 'j')] = ('k', 1)
mtab[('i', 'k')] = ('j', -1)

mtab[('j', '1')] = ('j', 1)
mtab[('j', 'i')] = ('k', -1)
mtab[('j', 'j')] = ('1', -1)
mtab[('j', 'k')] = ('i', 1)

mtab[('k', '1')] = ('k', 1)
mtab[('k', 'i')] = ('j', 1)
mtab[('k', 'j')] = ('i', -1)
mtab[('k', 'k')] = ('1', -1)

def mult(x, y):
    z = mtab[(x[0], y[0])]
    return (z[0], x[1]*y[1]*z[1])

def pow_q(x, p):
    if p == 1:
        return x

    if p%2 == 1:
        return mult(x, pow_q(x, p-1))

    r = pow_q(x, p/2)
    return mult(r, r)

CACHE = {}
def reduce_r(s):
    if s in CACHE:
        return CACHE[s]

    if len(s) == 1:
        CACHE[s] = (s[0], 1)
        return (s[0], 1)

    x = s[:len(s)/2]
    y = s[len(s)/2:]
    res = mult(reduce_r(x), reduce_r(y))
    CACHE[s] = res
    return res

def solve_case(x, s):
    tot = x * len(s)
    if tot < 3:
        return "NO"

    base = reduce_r(s)
    if pow_q(base, x) != ('1', -1):
        return "NO"

    been_there_i = set()
    r_left = ('1', 1)
    i = 0
    x_used = 0
    while True:
        st = (r_left, i)
        if st in been_there_i:
            return "NO"
        been_there_i.add(st)

        r_left = mult(r_left, (s[i], 1))
        i += 1
        if i == len(s):
            i = 0
            x_used += 1
            if x_used == x:
                return "NO"
        if r_left == ('i', 1):
            break

    been_there_j = set()
    r_left = ('1', 1)
    while True:
        st = (r_left, i)
        if st in been_there_j:
            return "NO"
        been_there_j.add(st)

        r_left = mult(r_left, (s[i], 1))
        i += 1
        if i == len(s):
            i = 0
            x_used += 1
            if x_used == x:
                return "NO"
        if r_left == ('j', 1):
            break

    return "YES"

T = int(raw_input())
for t in xrange(T):
    X = int(raw_input().rstrip().split()[1])
    S = raw_input().rstrip()
    print "Case #%d: %s" % (t+1, solve_case(X, S))
