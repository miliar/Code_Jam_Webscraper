#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import random

def solve(H, D, S):

  #print H, D, S
  N = len(H)
  assert N == len(D)
  Q = len(S)
  C = [None for i in xrange(N)]
  C[N-1] = 0.0
  for i in xrange(N - 2, -1, -1):
    #print i
    t  = 0.0
    for j in xrange(i+1, N):
      #print i, j
      t += D[j-1][j]
      #print t, D[j-1][j]
      if t > H[i][0]:
        break
      if C[j] == None:
        continue
      cost = (t / H[i][1]) + C[j]
      if C[i] == None or cost < C[i]:
        C[i] = cost
    #print C

  #print C
      

  return "%.6f" % C[0]

def solve(H, D, S):

  #print H, D, S

  #print H, D, S

  N = len(H)
  assert N == len(D)
  Q = len(S)
  F = [[-1 for i in xrange(N)] for j in xrange(N)]
  for i in xrange(N):
    F[i][i] = 0

  for i in xrange(N):
    for j in xrange(N):
      if D[i][j] != -1:
        F[i][j] = D[i][j]

  for k in xrange(N):
    for i in xrange(N):
      for j in xrange(N):
        if F[i][k] != -1 and F[k][j] != -1 and (F[i][j] == -1 or F[i][k] + F[k][j] < F[i][j]):
          F[i][j] = F[i][k] + F[k][j]

  #print F

  G = [[-1 for i in xrange(N)] for j in xrange(N)]
  for i in xrange(N):
    G[i][i] = 0.0

  for i in xrange(N):
    for j in xrange(N):
      if F[i][j] != -1 and F[i][j] <= H[i][0]:
        G[i][j] = float(F[i][j]) / H[i][1]

  #print G

  for k in xrange(N):
    for i in xrange(N):
      for j in xrange(N):
        if G[i][k] != -1 and G[k][j] != -1 and (G[i][j] == -1 or G[i][k] + G[k][j] < G[i][j]):
          G[i][j] = G[i][k] + G[k][j]


  ##print G

  result = " ".join(["%.6f" % G[i-1][j-1] for (i, j) in S])
  return result

total = None
count = 0
f = sys.stdin

count = None
N, Q = None, None
tests = []
for line in sys.stdin:
  if not count:
    count = int(line.strip())
    continue
  elif N == None:
    N, Q = [int(x) for x in line.strip().split()]
    H = []
    D = []
    S = []
  elif len(H) < N:
    H.append([int(x) for x in line.strip().split()])
  elif len(D) < N:
    D.append([int(x) for x in line.strip().split()])
  else:
    S.append([int(x) for x in line.strip().split()])
    if len(S) == Q:
      tests.append((H, D, S))
      N, Q = None, None

#print count, tests

if count != len(tests):
  print "Wrong number of test cases"
  sys.exit(0)

counter = 0
for g in tests:
  counter += 1
  #print t
  print "Case #%d: %s" % (counter, solve(*g))
  #sys.exit()



