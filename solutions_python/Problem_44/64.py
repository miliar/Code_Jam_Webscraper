#! /usr/bin/env python
import sys, re, math
# some reading functions
getline = lambda f: f.readline().strip()
gettoken = lambda f: re.split("\s+", getline(f))
getint = lambda f: int(getline(f))
getints = lambda f: map(int, gettoken(f))

# number theory / combinatorics
product = lambda l: reduce(lambda x,y: x*y, l) if l else 1
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

f = open(sys.argv[1]) # open file

[N] = getints(f)
for cases in xrange(0,N): # loop over cases
    ans = 0
    # main

    n = getint(f)

    s = [0.0]*6
    for i in xrange(n):
        s = map(lambda x,y:x+y, s, getints(f))
    p = s[:3]
    v = s[3:]
    vp = sum(map(lambda x,y:x*y, p, v))
    vv = sum(map(lambda x,y:x*y, v, v))

    if vv == 0: 
        t = 0
    else:
        t = -1.0*vp / vv
    
    if t < 0: t = 0

    d = map(lambda x, y: x + y*t, p, v)
    dd = math.sqrt(sum(map(lambda x,y:x*y, d, d)) / float(n)**2)

    # main
    print "Case #%d: %.8f %.8f"%( cases+1, dd, t ) # answer output