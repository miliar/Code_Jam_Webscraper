#!/usr/bin/env python
import os,sys,string

def gcd(a, b):
  while (b != 0):
    temp = a % b
    a = b
    b = temp
  return abs(a)

def lcm(a, b):
  gcd_value = gcd(a, b)
  if (gcd_value == 0): return 0
  return abs( (a * b) / gcd_value )

fp = open(sys.argv[1], 'rt')
T = int(fp.readline().strip())
for trial in range(T):
  data = map(lambda x: int(x), fp.readline().strip().split())
  B, N = data[0], data[1]
  Blst = map(lambda x: int(x), fp.readline().strip().split())
  lcmval = reduce(lcm, Blst)

  if B > N:
    print "Case #%d: %d" % (trial + 1, N)
    continue

  ary = [0 for i in range(0, lcmval + 1)]
  for n in range(len(Blst)):
    for u in range(1, (lcmval / Blst[n]) + 1):
      ary[(u * Blst[n])] += 1

  selected, reamined = 0, 0
  num = (N - B) % sum(ary)
  if num == 0: 
    print "Case #%d: %d" % (trial + 1, B)
    continue

  for n in range(1, lcmval + 1):
    num -= ary[n]
    if num <= 0:
      remained = num + ary[n]
      selected = n
      break

  for n in range(len(Blst)):
    if selected % Blst[n] == 0:
      if remained == 1:
        print "Case #%d: %d" % (trial + 1, n + 1)
        break
      remained -= 1
