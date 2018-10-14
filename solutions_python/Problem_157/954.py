#!/usr/bin/python

import sys, math

def mult(a,b):
  if a == '1': # +1 * ?
    return b
  elif b == '1': # ? * +1
    return a
  elif a == '-': # -1 * ?
    if b == '1':
      return '-'
    elif b == '-':
      return '1'
    elif b in 'ijk':
      return b.upper()
    else:
      return b.lower()
  elif b == '-': # ? * -1
    return mult(b,a)
  elif a == 'i': # +i * ?
    if b == 'i':
      return '-'
    elif b == 'j':
      return 'k'
    elif b == 'k':
      return 'J'
    elif b == 'I':
      return '1'
    elif b == 'J':
      return 'K'
    elif b == 'K':
      return 'j'
    else:
      print >> sys.stderr, "bad:",b
      raise
  elif a == 'j': # +j * ?
    if b == 'i':
      return 'K'
    elif b == 'j':
      return '-'
    elif b == 'k':
      return 'i'
    elif b == 'I':
      return 'k'
    elif b == 'J':
      return '1'
    elif b == 'K':
      return 'I'
    else:
      print >> sys.stderr, "bad:",b
      raise
  elif a == 'k': # +k * ?
    if b == 'i':
      return 'j'
    elif b == 'j':
      return 'I'
    elif b == 'k':
      return '-'
    elif b == 'I':
      return 'J'
    elif b == 'J':
      return 'i'
    elif b == 'K':
      return '1'
    else:
      print >> sys.stderr, "bad:",b
      raise
  elif a in 'IJK': # -{i,j,k} * ?
    A = a.lower()
    return mult('-',mult(A,b))
  else:
    print >> sys.stderr, "bad:",a
    raise

def mult_str(S):
  x = '1'
  for c in S:
    x = mult(x, c)
  return x

def greedy(S, L, ss, needles, start=0):
  # print >> sys.stderr, "greedy",needles,start

  if len(needles) == 0:
    return start >= len(S)
  elif start >= len(S):
    return False
  elif len(needles) == 1:
    return mult_special(S, L, ss, start) == needles

  x = '1'
  needle = needles[0]

  for i in range(start, len(S)):
    c = S[i]
    # print >> sys.stderr, x,'*',c,'=',
    x = mult(x, c)
    # print >> sys.stderr, x

    if x == needle:
      if len(needles) == 2: # if there are only 2, then any movements are by groups which equal 1
        return greedy(S, L, ss, needles[1:], i+1)
      else:
        if greedy(S, L, ss, needles[1:], i+1):
          return True

    if (i-start) >= L*3:
      return False
  return False

def mult_special(S, L, ss, start):
  x = '1'

  n = int(math.ceil(float(start) / L) * L)
  for i in range(start, n):
    c = S[i]
    x = mult(x, c)

  d = (len(S) - n) / L
  while d > 0:
    if d >= 4: # ? * ? * ? * ? = 1
      d -= 4
    else:
      x = mult(x, ss)
      d -= 1

  # print >> sys.stderr, mult_str(S[start:]), x # check
  return x

T = int(sys.stdin.readline())
for test in range(T):
  # for a in '1ijk':
  #   for b in '1ijk-IJK':
  #     print >> sys.stderr, mult(a,b),
  #   print >> sys.stderr, ""

  print >> sys.stderr, "Test: %d" % (test+1)
  toks = sys.stdin.readline().strip().split()
  L = int(toks[0])
  X = int(toks[1])
  s = sys.stdin.readline().strip()
  ss = mult_str(s)
  S = s * X
  # print >> sys.stderr, L, X, s, ss, S

  r = greedy(S, L, ss, 'ijk')
  # print greedy('ijk', 'ijk')

  if r:
    print "Case #%d: YES" % (test+1)
  else:
    print "Case #%d: NO" % (test+1)

