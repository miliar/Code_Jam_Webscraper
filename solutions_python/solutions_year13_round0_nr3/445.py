#!/usr/bin/env python

from numpy import *

def slurp(fname):
  with open(fname,"r") as f:
    l = f.readline()
    while l:
      yield l[:-1]
      l = f.readline()

def ints(l):
  return [int(x) for x in l.split(" ") if x != ""]


def load(fname):
  ll = [ints(l) for l in slurp(fname)]
  T  = ll[0][0]
  ll = ll[1:(T+1)]
  return ll

def mirror(s, p):
  sr = s[::-1]
  if p: return s + sr[1:]
  else: return s + sr

def is_odd(x): return (x&1) == 1
def is_even(x): return (x&1) == 0

def is_palindrom(x):
  s = str(x)
  return s == s[::-1]  

def next_p(x):
  s    = str(x)
  n    = len(s)
  half = (n+1)/2 #Include middle when odd
  s_   = s[:half]
  h    = str(int(s_)+1)
  x_   = int(mirror(s_, is_odd(n) ))

  if x_ > x        : return x_
  if is_even(n)    : return int( mirror(h, len(h) > half) )
  if len(h) == half: return int( mirror(h,True) )

  return int( mirror(h[:-1],False) )

def palindrome_seq(start):
  x = 0 if start == 0 else next_p(start-1)
  while True:
    yield x
    x = next_p(x)

def fair_square_seq(s,e):
  s_ = int(sqrt(s))
  for x in palindrome_seq(s_):
    xx = x*x
    if xx > e:
      return 
    if xx >= s and is_palindrom(xx):
      yield xx
  
  
def solve(p):
  s,e = p
  n = len([x for x in fair_square_seq(s,e)])
  return str(n)


if __name__ == "__main__":
  import sys
  
  pp = load(sys.argv[1])

  for i,p in enumerate(pp,1):
    r = solve(p)
    print "Case #%d: %s" % (i,r)

