#!/usr/bin/env python

from itertools import permutations

def diff(A, B):
  s, n = 0, len(A)
  for i in xrange(n):
    for j in xrange(n):
      s += B[i][j] - A[i][j]
  return s

def valid(A, B):
  n = len(A)
  for i in xrange(n):
    for j in xrange(n):
      if B[i][j] < A[i][j]:
        return False
  return True

def satisfied(A, taken):
  n = len(A[0])
  s = False
  for i in xrange(n):
    if A[0][i]==1 and taken[i]==0:
      s = True
      tmptaken = taken[:]
      tmptaken[i] = 1
      if len(A) == 1:
        return True
      if len(A) > 1 and not satisfied(A[1:], tmptaken):
        return False
  return s

def next(A):
  n = len(A)
  s = ''.join([''.join([str(x) for x in y]) for y in A])
  c = int(s, 2) + 1
  if c >= 2**(n*n):
    return None
  else:
    c = bin(c)[2:].zfill(n*n)
    B = [[int(x) for x in c[i:i+n]] for i in xrange(0, n*n, n)]
    return B

for nnn in xrange(1, int(raw_input())+1):
  print "Case #%d:" % (nnn),
  N = int(raw_input())
  M = [0]*N
  for i in xrange(N):
    S = raw_input().strip()
    M[i] = [int(x) for x in S]
  B = [[0]*N for i in xrange(N)]
  min_cost = N*N
  while min_cost > 0:
    B = next(B)
    if B is None:
      break
    if not valid(M, B):
      continue
    bad = False
    for C in permutations(B):
      if not satisfied(C, [0]*N):
        bad = True
    if bad:
      continue
    cost = diff(M, B)
    min_cost = min(min_cost, cost)
  print min_cost

