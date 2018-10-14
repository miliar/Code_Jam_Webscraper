#!/usr/bin/python
import sys
from math import sqrt
import mpmath
mpmath.mp.prec=300


map={}
def dynamic_programming(func):
  def decorator(*args, **kwargs):
      if (func,args) in map:
          return map[(func,args)]
      else:
          r = func(*args, **kwargs)
          map[(func,args)] = r
          return r
  return decorator

@dynamic_programming
def factorize(n):
    fp = primes(n)
    factors = []
    for i in fp:
        f = n%i
        while f ==0:
            factors.append(i)


@dynamic_programming
def primes(n): 
    nroot = int(sqrt(n))
    sieve = range(n+1)
    sieve[1] = 0

    for i in xrange(2, nroot+1):
        if sieve[i] != 0:
            m = n/i - i
            sieve[i*i: n+1:i] = [0] * (m+1)

    sieve = [x for x in sieve if x !=0]

    return sieve

@dynamic_programming
def f(n):
    if n==1:
        return 3 + mpmath.mpf(5)**0.5
    else:
        return f(n-1)*f(1)

@dynamic_programming
def fib(x):
  if x==0:
      return 0
  if x==1:
      return 1
  return fib(x-1)+fib(x-2)


def resolve(a):
    
    return str(f(a) +1000).split(".")[0][-3:]



fd = open(sys.argv[1])
n = int(fd.readline()[:-1])

out=[]
for I in xrange(n):
    m = int(fd.readline()[:-1])
    out.append("Case #%d: %s"%(I+1,resolve(m)))  

print "\n".join(out)
