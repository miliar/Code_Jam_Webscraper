#!/usr/bin/env python3
# encoding: utf-8

import sys
import math
from pprint import pprint


def solveCase(r, c, m):
  board = [['*'] * c for i in range(r)]
  board[0][0] = 'c'

  s = r * c - m
  if s == 1:
    return board

  if c == 1:
    for i in range(1, r - m):
      board[i][0] = '.'      
    return board

  if r == 1:
    for i in range(1, c - m):
      board[0][i] = '.'      
    return board    

  if c == 2:
    if (m % 2) != 0:
      return False
    if (m // 2) > (r - 2):
      return False
    for i in range(0, r - (m // c)):
      for j in range(c):
        board[i][j] = '.'

    board[0][0] = 'c'
    return board

  if r == 2:
    if (m % 2) != 0:
      return False
    if (m // 2) > (c - 2):
      return False
    for j in range(0, c - (m // r)):
      for i in range(r):
        board[i][j] = '.'

    board[0][0] = 'c'
    return board

  if m < (r - 2) * (c - 2):
    for i in [0, 1]:
      for j in range(c):
        if (i, j) != (0, 0):
          board[i][j] = '.'
      for j in range(r):
        if (i, j) != (0, 0):
          board[j][i] = '.'

    s = (r - 2) * (c - 2) - m
    for i in range(r - 2):
      for j in range(c - 2):
        board[2 + i][2 + j] = '.'
        s -= 1
        if s == 0:
          return board
 
  s = r * c - m

  board[0][1] = '.'
  board[1][0] = '.'
  board[1][1] = '.'

  if (s < 4) or (s == 5) or (s == 7):
    return False

  if (s % 2) == 1:
    board[2][2] = '.'

  p = s // 2 - 2
  i = 2
  j = 2
  while p > 0:
    if i < c:
      board[0][i] = '.'
      board[1][i] = '.'
      i += 1
      p -= 1
      if p == 0:
        break

    if j < r:
      board[j][0] = '.'
      board[j][1] = '.'
      j += 1
      p -= 1

  return board

def checkBoard(res, rw, c, m):
  count = 0
  for i in range(rw):
    for j in range(c):
      if res[i][j] == '*':
        count += 1

  return (m == count)
def solve(s):
  t = int(s.readline())

  for i in range(t):
    rw, c, m = [int(i) for i in s.readline().split()]
    
    print('Case ' + str(i + 1))
    r = solveCase(rw, c, m)
    if r == False:
      sp = rw * c - m
      print(sp, rw, c, m)
      yield 'Impossible\n'
    else:
      result = ''
      for row in r:
        result += ''.join(row) + '\n'
      if not checkBoard(r, rw, c, m):
        print('error')
      yield result

def main(argv=None):
  fileName = argv[1]
  s = open(fileName)
  r = open(fileName + '.result.txt'  , 'w')

  result = solve(s)
  for i, case in enumerate(result, 1):
    r.write('Case #' + str(i) + ': \n' + case)
        
  return 0

if __name__ == '__main__':
  status = main(sys.argv)
  sys.exit(status)
