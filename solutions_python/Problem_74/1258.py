#!/usr/bin/python

TESTS = int(raw_input())

global moves

def move(p, l):
  global moves
  for move in moves:
    if move[1] == l:
      if move[0] > p: return p+1
      elif move[0] < p: return p-1
      else: break

  return p


for N in range(1, TESTS+1):
  line = raw_input().strip().split(' ')[1:]
  moves = []
  while line:
    (c, p) = line[:2]
    moves.append((int(p), c))
    line = line[2:]

  pO, pB = 1, 1

  k = 0
  while moves:
    if moves[0] == (pO, 'O'):
      moves = moves[1:]
      pB = move(pB, 'B')
    elif moves[0] == (pB, 'B'):
      moves = moves[1:]
      pO = move(pO, 'O')
    else:
      pO = move(pO, 'O')
      pB = move(pB, 'B')
    k += 1

  print 'Case #'+str(N)+': '+str(k)
