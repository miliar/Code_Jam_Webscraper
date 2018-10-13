#!/usr/bin/python

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

C = int(raw_input())

for tc in range(C):
  inp = map(long, raw_input().split())
  n = inp[0]
  vec = inp[1:]
  vec = list(set(vec))
  vec.sort()
  total_gcd = vec[1] - vec[0]
  for i in range(2, len(vec)):
    cdiff = vec[i] - vec[i-1]
    total_gcd = gcd(total_gcd, cdiff)
  # print total_gcd
  md = (total_gcd - vec[0] % total_gcd) % total_gcd
  print "Case #%d: %s" % (tc + 1, md)
