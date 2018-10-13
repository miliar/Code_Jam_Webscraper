#! /usr/bin/env python
import sys, re
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

class Node:
    def __init__(self):
        self.kid = {}
    def isin(self, s):
        return s in self.kid
    def add(self, s):
        if not self.isin(s): self.kid[s] = Node()
    def get(self, s):
        return self.kid[s]
    def degree(self):
        s = 1
        for k in self.kid.itervalues():
            s += k.degree()
        return s
    def __repr__(self):
        return str(self.kid)

if __name__ == "__main__":
    f = open(sys.argv[1]) # open file

    [N] = getints(f)
    for cases in xrange(0,N): # loop over cases
        ans = 0
        # main
        root = Node()

        n, m = getints(f)
        for i in xrange(n): # existing
            path = getline(f)
            folders = path.split('/')[1:]
            
            r = root
            for folder in folders:
                r.add(folder)
                r = r.get(folder)
        d1 = root.degree()

        for j in xrange(m): # new
            path = getline(f)
            folders = path.split('/')[1:]
            
            r = root
            for folder in folders:
                r.add(folder)
                r = r.get(folder)
        d2 = root.degree()
        ans = d2 - d1

        # main
        print "Case #%d: %d"%( cases+1, ans ) # answer output
