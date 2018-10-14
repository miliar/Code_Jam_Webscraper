#!/usr/bin/env python

T = int(raw_input())

def read_problem():
  n = int(raw_input())
  naomi = [ float(e) for e in raw_input().split() ]
  ken = [ float(e) for e in raw_input().split() ]
  return n, naomi, ken

def naomiWar(naomi):
  # choose the highest
  naomiI = len(naomi) - 1
  naomiT = naomi[naomiI]
  return naomiI, naomiT

def kenWar(naomiW, ken):
  kenI = len(ken) - 1
  if ken[kenI] > naomiW: # ken can win
    while kenI > 0 and ken[kenI-1] > naomiW:
      kenI -= 1
  else: # ken lost, play the smallest
    kenI = 0
  return kenI

def naomiDeceitfulWar(naomi, ken):
  naomiI = len(naomi) - 1
  naomiT = naomi[naomiI]
  kenI = kenWar(naomiT, ken)
  if ken[kenI] > naomiT:
    # ken will win, choose the smallest suitable
    return 0, naomiT
  else:
    # naomi will win, choose the smallest suitable
    while naomiI > 0 and naomi[naomiI - 1] > ken[kenI]:
      naomiI -= 1
    return naomiI, naomiT

def solve(problem):
  n, naomi, ken = problem
  naomi.sort()
  naomi1 = naomi[:]
  ken.sort()
  ken1 = ken[:]
  # both War
  naomiP, kenP = 0, 0
  while naomi:
    naomiI, naomiT = naomiWar(naomi)
    kenI = kenWar(naomiT, ken)
    if naomi.pop(naomiI) > ken.pop(kenI):
      naomiP += 1
    else:
      kenP += 1
  naomiWarS = naomiP
  #
  naomi, ken = naomi1, ken1
  # naomi DeceitWar
  naomiP, kenP = 0, 0
  while naomi:
    naomiI, naomiT = naomiDeceitfulWar(naomi, ken)
    kenI = kenWar(naomiT, ken)
    if naomi.pop(naomiI) > ken.pop(kenI):
      naomiP += 1
    else:
      kenP += 1
  naomiDWarS = naomiP
  return naomiDWarS, naomiWarS

for n in range(T):
  problem = read_problem()
  solution = solve(problem)
  print 'Case #%d: %d %d' %(n+1, solution[0], solution[1])

