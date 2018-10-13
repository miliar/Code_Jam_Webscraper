#!/usr/bin/env python3
# encoding: utf-8

import sys
import math
from pprint import pprint

def qm(a, b):
  neg = False
  
  if a[0] == '-':
    neg = True
    a = a[1:]
  
  if b[0] == '-':
    neg = not neg
    b = b[1:]

  t = {
    '1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
    'i': {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'},
    'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
    'k': {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'}
    }

  c = t[a][b]

  if not neg:
    return c
  
  if c[0] == '-':
    return c[1:]
  
  return '-' + c
  
def find(s, a, i, p):
  #print(s,a,i)
  r = '1'
  for j in range(i, len(s)):
    if s[j] == '*':
      r = qm(r, p)  
    else:
      r = qm(r, s[j])  
    
    if r == a:
      return True, j + 1

  return False, 0

def pow(s, p):
  r = '1'
  for c in s:
    r = qm(r, c)
  
  i = r
  p = p % 4
  if p == 0:
    return '1'

  for j in range(1, p):
    i = qm(i, r)

  return i

def solveCase(s, x):
  if x < 17:
    s = s * x
    p = '1'
  else:
    p = pow(s, x - 16)
    s = s * 8 + '*' + s * 8

  f, i = find(s, 'i', 0, p)
  if not f:
    return 'NO'
  
  f, i = find(s, 'j', i, p)
  if not f:
    return 'NO'

  f, i = find(s, 'k', i, p)
  if not f:
    return 'NO'

  while i < len(s):
    f, i = find(s, '1', i, p)
    if not f:
      return 'NO'

  return 'YES'
  

def solve(s):
  t = int(s.readline())
  
  for i in range(t):
    l, x = [int(k) for k in s.readline().split()]
    yield solveCase(s.readline().strip(), x)

def main(argv=None):
  fileName = argv[1]
  s = open(fileName)
  r = open(fileName + '.result.txt'  , 'w')

  result = solve(s)
  for i, case in enumerate(result, 1):
    r.write('Case #' + str(i) + ': ' + case + '\n')
        
  return 0

if __name__ == '__main__':
  status = main(sys.argv)
  sys.exit(status)