#!/usr/bin/env python3

from __future__ import division, print_function

try:
  input = raw_input
  range = xrange
except NameError:
  pass

def isqrt(n):
  if n == 0:
    return 0

  a = (n.bit_length() + 1)//2

  x = 1 << a
  while True:
    y = (x + n//x)//2
    if y >= x:
      break
    x = y

  return x

def is_palindrome(n):
  s = str(n)
  return s == s[::-1]

def palindromes(m, n):
  sm = str(m)
  q, r = divmod(len(sm), 2)
  h = int(sm[:(q + r)])

  while True:
    sh = str(h)

    if len(sh) != q + r:
      if r == 0:
        r = 1
      else:
        q, r = q + 1, 0
        h = h//10
        sh = sh[:-1]

    if r == 0:
      w = int(sh + sh[::-1])
    else:
      w = int(sh + sh[-2::-1])

    if w >= n:
      return
    elif w >= m:
      yield w

    h = h + 1

T = int(input())

for i in range(1, T + 1):
  line = input().split(' ')
  A = int(line[0])
  B = int(line[1])

  m = isqrt(A - 1) + 1
  n = isqrt(B)

  count = 0
  for j in palindromes(m, n + 1):
    if is_palindrome(j*j):
      count = count + 1

  print('Case #%d: %d' % (i, count))
