from collections import *
from itertools import *
import sys

def pairs2():
    p = [(10*t+u,10*u+t) 
         for t, u in product(range(10), repeat=2)]
    return set((x,y) for x,y in p if x!=y)

def pairs3():
    p =  ([(100*h + 10*t + u, 100*t+10*u+h) 
           for h, t, u in product(range(10), repeat=3)
           if h != 0 and t != 0] +
          [(100*h + 10*t + u, 100*u+10*h+t) 
           for h, t, u in product(range(10), repeat=3)
           if h != 0 and u != 0])
    return set((x,y) for x,y in p if x!=y)

def pairs4():
    p =  (
        [(1000*m + 100*h + 10*t + u, 1000*h+100*t+10*u+m) 
         for m, h, t, u in product(range(10), repeat=4)
         if m != 0 and h != 0] +
        [(1000*m + 100*h + 10*t + u, 1000*t+100*u+10*m+h) 
         for m, h, t, u in product(range(10), repeat=4)
         if m != 0 and t != 0] +
        [(1000*m + 100*h + 10*t + u, 1000*u+100*m+10*h+t) 
         for m, h, t, u in product(range(10), repeat=4)
         if m != 0 and u != 0])
    return set((x,y) for x,y in p if x!=y)

p2 = pairs2()
p3 = pairs3()
p4 = pairs4()

def inrange(x, a, b):
    return x>=a and x<=b

def solve(a, b):
    r = 0
    if inrange(a, 10, 99):
        assert inrange(b, 10, 100)
        r = sum(1 for x, y in p2 if inrange(x, a, b) and inrange(y, a, b))
    if inrange(a, 100, 999):
        assert inrange(b, 100, 999)
        r = sum(1 for x, y in p3 if inrange(x, a, b) and inrange(y, a, b))
    if inrange(a, 1000, 9999):
        assert inrange(b, 1000, 9999)
        r = sum(1 for x,y in p4 if inrange(x, a, b) and inrange(y, a, b))
    return r//2

L = list(sys.stdin)
for t in range(1, 1+int(L[0])):
    print 'Case #%d: %d' % (t,solve(*map(int, L[t].split())))
