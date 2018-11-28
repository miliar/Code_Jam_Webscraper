#!/usr/bin/env python

from math import sqrt

N = 4
T = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def ans(a, b):
  count = 0
  left = 0
  for i in xrange(len(T)):
    if T[i] &gt; b:
      break
    if T[i] &gt;= a:
      r = int(sqrt(T[i]))
      if r * r == T[i] and check_palindrome(r):
        count = count + 1
  return count

def check_palindrome(x):
  xs = list(str(x))
  i, j = 0, len(xs) - 1
  while i &lt; j:
    if xs[i] != xs[j]:
      return False
    i = i + 1
    j = j - 1
  return True

def build_table():
  for i in xrange(2, N + 1):
    l = i / 2
    r = i % 2
    gen = []
    for j in xrange(1, 10**l):
      if j % 10 == 0:
        continue
      t = str(j)
      if j &lt; 10**(l-1):
        t = ''.join(('0', t))
      rt = ''.join(reversed(list(t)))
      if r == 1:
        for m in xrange(10):
          z = ''.join((rt, str(m), t))
          gen.append(int(z))
      else:
        z = ''.join((rt, t))
        gen.append(int(z))
    T.extend(gen)

def main():
  cases = int(raw_input())
  for case in xrange(cases):
    a, b = map(lambda x: int(x), raw_input().split())
    print 'Case #%d: %d' % (case + 1, ans(a, b))

if __name__ == '__main__':
  build_table()
  main()
