#!/usr/bin/env python3

import sys

def best_ken(chosen_naomi, ken):
  try:
    chosen_ken = min(w for w in ken if w > chosen_naomi)
  except ValueError:
    chosen_ken = min(ken)
  ken.remove(chosen_ken)
  return chosen_ken

def max_two(ken):
  first_max = -1
  second_max = -1
  for w in ken:
    if w > first_max:
      second_max = first_max
      first_max = w
    elif w > second_max:
      second_max = w
  assert first_max != 0 and second_max != 0
  return (first_max, second_max)

def best_deceitful_naomi(naomi, ken):
  min_ken = min(ken)
  try:
    chosen_naomi = min(w for w in naomi if w > min_ken)
    told_naomi = max(ken) + 1
  except ValueError:
    chosen_naomi = min(naomi)
    first_max, second_max = max_two(ken)
    if first_max < chosen_naomi:
      told_naomi = chosen_naomi
    else:
      told_naomi = (first_max + second_max) / 2.0
  naomi.remove(chosen_naomi)
  return told_naomi, chosen_naomi

def war(N, naomi, ken):
  score = 0
  for i in range(N):
#    print(i, naomi, ken, file=sys.stderr)
    chosen_naomi = naomi.pop()
    chosen_ken = best_ken(chosen_naomi, ken)
    if chosen_naomi > chosen_ken:
      score += 1
  return score

def deceitful_war(N, naomi, ken):
  if N == 0:
    return 0
  score = 0
  for i in range(N):
#    print(i, naomi, ken, file=sys.stderr)
    told_naomi, chosen_naomi = best_deceitful_naomi(naomi, ken)
    chosen_ken = best_ken(told_naomi, ken)
    assert ((chosen_naomi > chosen_ken) | (told_naomi <= chosen_ken))
    if chosen_naomi > chosen_ken:
      score += 1
  return score

def solve(problem):
  N, naomi, ken = problem
#  print(N, list(sorted(naomi)), list(sorted(ken)), sep="\n", file=sys.stderr)
  return (deceitful_war(N, set(naomi), set(ken)), war(N, set(naomi), set(ken)))

def read():
  N = int(input())
  naomi = set(map(float, input().split()))
  ken = set(map(float, input().split()))
  return (N, naomi, ken)

def write(i, solution):
  dw, w = solution
  print("Case #%d: %d %d" % (i + 1, dw, w))

def main():
  cases = int(input())
  for i in range(cases):
    problem = read()
    solution = solve(problem)
    write(i, solution)

if __name__ == "__main__":
  main()

