#! /usr/bin/env python
import sys, re
import operator as op
import math

""" START TEMPLATE JCHAOISAAC """

# some reading functions
getline = lambda f: f.readline().strip()
gettoken = lambda f: re.split("\s+", getline(f))
getint = lambda f: int(getline(f))
getints = lambda f: map(int, gettoken(f))

# number theory / combinatorics
product = lambda l: reduce(op.mul, l) if l else 1
factorial = lambda n: product(xrange(n, 1, -1))
nPr = lambda n, r: product(xrange(n,n-r,-1))
nCr = lambda n, r: nPr(n, r) / factorial(r)
nMr = lambda l: factorial(sum(l)) / product(map(factorial,l))
gcd = lambda x,y: gcd(y, x%y) if y != 0 else x
lcm = lambda x,y: x * y / gcd(x, y)
def gcd2(a, b):
    if b == 0: return (a, 1, 0)
    (d,x,y) = gcd2(b, a % b)
    return (d, y, x - a / b * y)
isSq = lambda n: n == int(math.sqrt(n)) ** 2
def primes(n):
    if n == 2: return [2]
    if n < 2: return []
    s = range(3, n+1, 2)
    mroot = n ** 0.5
    half = (n + 1) / 2 - 1
    i, m=0, 3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i += 1
        m = 2*i + 3
    return [2]+[x for x in s if x]
def factorize(n):
    factors = []
    c = 0
    while n % 2 == 0: n, c = n/2, c+1
    if c != 0: factors.append((2, c))
    if n == 1: return factors
    for i in xrange(3, n+1, 2):
        c = 0
        while n % i == 0: n, c = n/i, c+1
        if c != 0: factors.append((i, c))
        if n == 1: break
    return factors
def phi(n):
    fact = factorize(n)
    return product(map(lambda (p,n): p**(n-1) *(p - 1), fact))

# vector / geometry
cross = lambda u,v: u[0]*v[1] - u[1]*v[0]
add = lambda u,v: map(op.add, u, v)
sub = lambda u,v: map(op.sub, u, v)
scale = lambda u,s: map(lambda x: x*s, u)
neg = lambda u: map(op.neg, u)
mul = lambda u,v: map(op.mul, u, v)
dot = lambda u,v: sum(mul(u, v))
norm2 = lambda u: dot(u, u)
norm = lambda u: math.sqrt(norm2(u))
dist = lambda u,v: norm(sub(u, v))
dist2 = lambda u,v: norm2(sub(u, v))
def normalize(u):
    d = norm(u)
    if d == 0: return u
    return scale(u, 1.0/d)
turn = lambda u,v,w: cross(sub(v, u), sub(w, v))
straddle = lambda u,v,w,x: turn(u,v,w)*turn(u,v,x) < 0
intersect = lambda u,v,w,x: straddle(u,v,w,x) and straddle(w,x,u,v)

""" END TEMPLATE JCHAOISAAC """

f = open(sys.argv[1]) # open file

# global data



# global data

[T] = getints(f)
for cases in xrange(1,T+1): # loop over cases
    ans = 0
    # main

    combining, opposing, oppcount = {}, {}, {}
    token = gettoken(f)
    # combining
    C = int(token[0])
    Cs, token = token[1:C + 1], token[C + 1:]
    for comb in Cs:
        b1, b2, t = comb
        combining[b1+b2] = t
        combining[b2+b1] = t
    # opposing
    D = int(token[0])
    Ds, token = token[1:D + 1], token[D + 1:]
    for opp in Ds:
        b1, b2 = opp
        if b1 not in opposing: opposing[b1] = []
        opposing[b1].append(b2)
        if b2 not in opposing: opposing[b2] = []
        opposing[b2].append(b1)

        oppcount[b1] = 0
        oppcount[b2] = 0

    oppcount_blank = oppcount.copy();

    # sequence
    S = token[-1]

    stack = []
    ssize = 0
    for s in S:
        p = '' if ssize == 0 else stack[-1]
        comb = s + p
        if comb in combining:
            stack[-1] = combining[comb] # replace with boom
            if p in opposing: oppcount[p] -= 1
            continue
        elif s in opposing:
            cleared = False
            for opp in opposing[s]:
                if oppcount[opp] > 0:
                    stack = []
                    ssize = 0
                    oppcount = oppcount_blank.copy()
                    cleared = True
                    break
            if cleared:
                continue
            oppcount[s] += 1
        
        stack.append(s)
        ssize += 1

    ans = '[' + ', '.join(stack) + ']'

    # main
    print "Case #%d: %s"%( cases, ans ) # answer output


