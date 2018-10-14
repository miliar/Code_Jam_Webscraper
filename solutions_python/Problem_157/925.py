#!/usr/bin/env python

T = int(raw_input())

def read_problem():
  l, x = [ int(e) for e in raw_input().split() ]
  w = raw_input()
  return l, x, w

def qmult(x, y):
  s = x[0] * y[0]
  if x[1] == '1':
    if y[1] == '1':
      return (s, '1')
    elif y[1] == 'i':
      return (s, 'i')
    elif y[1] == 'j':
      return (s, 'j')
    elif y[1] == 'k':
      return (s, 'k')
  elif x[1] == 'i':
    if y[1] == '1':
      return (s, 'i')
    elif y[1] == 'i':
      return (-s, '1')
    elif y[1] == 'j':
      return (s, 'k')
    elif y[1] == 'k':
      return (-s, 'j')
  elif x[1] == 'j':
    if y[1] == '1':
      return (s, 'j')
    elif y[1] == 'i':
      return (-s, 'k')
    elif y[1] == 'j':
      return (-s, '1')
    elif y[1] == 'k':
      return (s, 'i')
  elif x[1] == 'k':
    if y[1] == '1':
      return (s, 'k')
    elif y[1] == 'i':
      return (s, 'j')
    elif y[1] == 'j':
      return (-s, 'i')
    elif y[1] == 'k':
      return (-s, '1')

def solve(problem):
  l, x, w = problem
  # eval w
  w_val = (1, w[0])
  for c in w[1:]:
    w_val = qmult(w_val, (1, c))
  #print w_val
  # sanity test
  if l * x < 3:
    return 'NO'
  if l * x == 3:
    if w == 'ijk':
      return 'YES'
    else:
      return 'NO'
  # all word in memory!
  s = w * x
  # find i
  i = 0
  v = (1, s[i])
  #print i, v
  while v != (1, 'i') and i + 1 < len(s):
    i += 1
    v = qmult(v, (1, s[i]))
    #print i, v
  if v != (1, 'i'):
    return 'NO'
  #print 'i at', i
  # find j
  if i + 1 >= len(s):
    return 'NO'
  i += 1
  v = (1, s[i])
  while v != (1, 'j') and i + 1 < len(s):
    i += 1
    v = qmult(v, (1, s[i]))
  if v != (1, 'j'):
    return 'NO'
  #print 'j at', i
  # find k
  if i + 1 >= len(s):
    return 'NO'
  i += 1
  v = (1, s[i])
  while i + 1 < len(s):
    i += 1
    v = qmult(v, (1, s[i]))
  if v != (1, 'k'):
    return 'NO'
  return str('YES')

for n in range(T):
  problem = read_problem()
  solution = solve(problem)
  print 'Case #%d: %s' %(n+1, solution)

