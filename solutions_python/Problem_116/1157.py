#!/usr/bin/env python
from numpy import array
import numpy as np

def chkrow(matrx):
  for i in range(4):
    eq = matrx[i][0]
    if eq == 'T':
      eq = matrx[i][1]
      start = 2
    else:
      start = 1
    if eq == '.':
      continue  
    found = True
    for j in range(start,4):
      c = matrx[i][j]
      if eq != c and c != 'T':
        found = False
        break
    if found:
      return eq
  return ''

def chkdiag(matrx):
  eq = matrx[0][0]
  if eq == 'T':
    eq = matrx[1][1]
    start = 2
  else:
    start = 1
  if eq == '.':
    return ''
  for i in range(start, 4):
    c = matrx[i][i]
    if eq != c and c != 'T':
      return ''
  return eq
    
def chkantdiag(matrx):
  eq = matrx[0][3]
  if eq == 'T':
    eq = matrx[1][2]
    start = 2
  else:
    start = 1
  if eq == '.':
    return ''
  for i in range(start, 4):
    c = matrx[i][3 - i]
    if eq != c and c != 'T':
      return ''
  return eq

def status(matrx, over):
  win = chkrow(matrx)
  if len(win) > 0:
    return "%s won" % win
  win = chkrow(np.transpose(matrx))
  if len(win) > 0:
    return "%s won" % win
  win = chkdiag(matrx)
  if len(win) > 0:
    return "%s won" % win
  win = chkantdiag(matrx)
  if len(win) > 0:
    return "%s won" % win
  if over:
    return "Draw"
  else:
    return "Game has not completed"
    
def main():
  cases = int(raw_input())
  for case in range(cases):
    case = case + 1
    matrx = []
    over = True
    for i in range(4):
      row = raw_input()
      if row.find('.') >= 0:
        over = False
      matrx.append(list(row))
    print "Case #%d: %s" % (case, status(array(matrx), over))
    if case != cases:
      raw_input()

main()
