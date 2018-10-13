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

    token = gettoken(f)
    moves = zip(token[1::2], map(int, token[2::2]))
    parallel, total = 0, 0
    pos = {"O": 1, "B": 1}
    prev = None
    for (type, val) in moves:
        d = abs(val - pos[type])
        pos[type] = val
        if not prev or prev == type: # same robot
            parallel += d + 1
        else: # diff robot
            total += parallel
            parallel = max(0, d - parallel) + 1
        prev = type
    ans = total + parallel
    
    # main
    print "Case #%d: %d"%( cases, ans ) # answer output


