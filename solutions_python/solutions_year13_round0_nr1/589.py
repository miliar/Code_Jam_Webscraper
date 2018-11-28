#!/usr/bin/env python

T = int(raw_input())

def read_problem():
  game = []
  game.append([c for c in raw_input()])
  game.append([c for c in raw_input()])
  game.append([c for c in raw_input()])
  game.append([c for c in raw_input()])
  raw_input()
  return game

def solve(game):
  lines = [set(line) for line in game]
  lines.append(set([line[0] for line in game]))
  lines.append(set([line[1] for line in game]))
  lines.append(set([line[2] for line in game]))
  lines.append(set([line[3] for line in game]))
  lines.append(set([game[r][r] for r in range(4) ]))
  lines.append(set([game[r][3-r] for r in range(4) ]))
  done = True
  for line in lines:
    if len(line) == 1:
      if 'X' in line:
        return 'X won'
      if 'O' in line:
        return 'O won'
    elif len(line) == 2:
      if 'X' in line and 'T' in line:
        return 'X won'
      if 'O' in line and 'T' in line:
        return 'O won'
    if '.' in line:
      done = False
  if not done:
    return 'Game has not completed'
  return 'Draw'

for n in range(T):
  problem = read_problem()
  solution = solve(problem)
  print 'Case #%d: %s' %(n+1, solution)

