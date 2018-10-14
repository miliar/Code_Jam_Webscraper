from os import sys
from copy import copy

def get_int():
  return int(sys.stdin.readline())

def get_blocks():
  return [float(s) for s in sys.stdin.readline().split()]

def deceitful_war(naiomi, ken):
  wins = 0
  n = len(naiomi)
  for i in range(n):
    if naiomi[0] > ken[0]:
      wins += 1
      ken.pop(0)
    else:
      ken.pop()
    naiomi.pop(0)
  return wins

def war(naiomi, ken):
  wins = 0
  n = len(naiomi)
  naiomi.reverse()
  ken.reverse()
  for i in range(n):
    if naiomi[0] > ken[0]:
      wins += 1
      ken.pop()
    else:
      ken.pop(0)
    naiomi.pop(0)
  return wins

num_cases = get_int()

for case in range(1,num_cases+1):
  num_blocks = get_int()
  naiomi = get_blocks()
  ken = get_blocks()
  naiomi.sort()
  ken.sort()

  y = deceitful_war(copy(naiomi), copy(ken))
  z = war(copy(naiomi), copy(ken))

  print "Case #" + str(case) + ":", y, z
