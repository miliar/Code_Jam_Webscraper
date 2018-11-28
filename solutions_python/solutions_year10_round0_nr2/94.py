#!/usr/bin/python

def gcd(a, b):
  while b != 0:
    t = a % b
    a = b
    b = t
  return a

T = input()
for t in range(1, T+1):
  s = raw_input()
  A = s.split()
  for i in range(0, len(A)): A[i] = int(A[i])
  N = A[0]
  A = A[1:]
  A.sort()
  D = A[1] - A[0]
  for i in range(1, len(A)):
    D = gcd(D, A[i]-A[i-1])
  R = A[0]
  if R % D != 0: R = R + D - (R % D)
  print "Case #%d: %d" % (t, R-A[0])
