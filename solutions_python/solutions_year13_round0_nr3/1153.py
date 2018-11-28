#!/usr/bin/python
# Language: Python 2.6.6

def rev(x):
  return x[::-1]

def get_palin_even(x):
  sx = str(x)
  return rev(sx) + sx

def get_palin_odd(x):
  sx = str(x)
  return rev(sx[1:]) + sx

def is_palin(x):
  tx = x
  y = 0
  while tx > 0:
    y *= 10
    y += tx % 10
    tx /= 10
  return y == x

legit = []
for i in range(1, 10000):
  if i % 10 != 0:
    for c in (get_palin_even(i), get_palin_odd(i)):
      ic = int(c)
      cand = ic * ic
      if is_palin(cand):
        legit.append(cand)

t = input()
for c in range(1, t+1):
  a, b = [int(x) for x in raw_input().split()]
  soln = 0
  for i in legit:
    if a <= i <= b:
      soln += 1
  print "Case #" + str(c) + ":", soln
