from __future__ import with_statement
from math import pow
from collections import defaultdict
from pprint import pprint as pp

import pickle
import pdb
import sys
import os
import math

from numpy import *

def parseIntLine(line):
  return [int(x) for x in line[:-1].split(" ")]

def main():
  with open(sys.argv[1],'r') as f:
    with open('test.out','w') as g:
      cases = int(f.readline()[:-1]) # number cases
      for j in range(cases):
        print j
        N,K = parseIntLine(f.readline())
        board = []
        for k in range(N):
          board.append(f.readline()[:-1])
        ans = computeAnswer(board, K)
        g.write("Case #%d: %s\n" % (j+1,ans))


def computeAnswer(board,K):
  board = [[c for c in x if c != '.'] for x in board]
  # pad it out
#   print board
  maxlen = max(len(x) for x in board)
  board = [['.']*(maxlen-len(x))+x for x in board if x]
#   print board
#   board = [list(x) for x in zip(*board)]

#   print board, maxlen
  #sentinel the board
  board = [['.']+x+['.'] for x in board]
  board = [['.']*(maxlen+2)] + board + [['.']*(maxlen+2)]
#   print board
  # for player Red
  # break out early
  foundR = findKRow(board, K, 'R')
  foundB = findKRow(board, K, 'B')

  #pp([[c for c in x if c ] for x in zip(*board)])
  if foundR and foundB:
    return "Both"
  elif foundR:
    return "Red"
  elif foundB:
    return "Blue"
  return "Neither"

def findKRow(board, K, p):
  # p is player char
  # search horizontals
  N = len(board)
  M = len(board[0])
  # search verticals
  for i in range(1,N-1):
    for j in range(1,M-1):
      # vertical
      found = True
      for k in range(K):
        if board[i+k][j] != p:
          found = False
          break
      if found:
        return True

      # horizontal
      found = True
      for k in range(K):
        if board[i][j+k] != p:
          found = False
          break
      if found:
        return True

      # diag down
      found = True
      for k in range(K):
        if board[i+k][j+k] != p:
          found = False
          break
      if found:
        return True

      # diag up
      found = True
      for k in range(K):
        if board[i-k][j+k] != p:
          found = False
          break
      if found:
        return True
  return False


if __name__=="__main__":
  main()


# import random
# test = ""
# for i in range(50):
#   for j in range(50):
#     if random.random() > 0.95:
#       test += "B"
#     else:
#       test += "R"
#   test += "\n"
# print test
