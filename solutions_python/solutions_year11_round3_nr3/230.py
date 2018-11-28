import sys

inputFile = sys.stdin
count = int(inputFile.readline())

import math

def primesToN(n):
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

def primes() :
    yield 2
    D = {}
    q = 3
    while True:
        p = D.pop(q, 0)
        if p:
            x = q + p
            while x in D: x += p
            D[x] = p
        else:
            yield q
            D[q*q] = 2*q
        q += 2

def primeFactor(n, primeSet = None, infinite = False) :
    sqrt = math.sqrt(n)
    if primeSet == None : 
        sqrt = math.sqrt(n)
        if infinite :
            primeSet = primes()
        else :
            primeSet = primesToN(int(sqrt))
    for p in primeSet :
        if sqrt and p > sqrt : break
        while n % p == 0 :
            yield p
            n /= p
    if n != 1: yield n

lineno = 1
for c in xrange(count):
  row = inputFile.readline().split()

  N, L, H = map(int, row)
  players = map(int, inputFile.readline().split())

  players = sorted(players)

  """
  primes = {}
  done = {}
  for p in players:
    if p not in done:
      done[p] = True
      for prime in primeFactor(p):
        primes[prime] = True

  num = 1
  for p in primes:
    num *= p
  """
  """
  bad = {1: True}
  for i in xrange(0, len(players)):
    for j in xrange(i+1, len(players)):
      a = players[i]
      b = players[j]
      if a == b or a == 1:
        continue
      if b % a == 0:
        bad[b] = True

  num = 1
  done = {}
  for p in players:
    if not p in bad and not p in done:
      done[p] = True
      num *= p
  """

  """
  if L <= num and num <= H:
    pass
  elif H < num:
    num = 'NO'
  else:
    l = 1.0 * L / num
    h = 1.0 * H / num
    for i in xrange(int(l), int(h)+1) :
      if i in primes:
        if L <= num * i and num * i <= H:
          num *= i
          break
   
    if num > H or num < L:
      num = 'NO'
  """

  def good(L, H, players):
    for i in xrange(L, H+1):
      good = True
      for p in players:
        if p % i != 0 and i % p != 0:
          good = False
          break
      if good:
        return i
    return 'NO'
  
  print "Case #%d:" % lineno, 

  print good(L, H, players)

  lineno += 1
