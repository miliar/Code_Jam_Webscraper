#!/usr/bin/python

from sys import stdin

def main():
  T = int(stdin.readline())
  for case in range(1, T + 1):
    solve_case(case)

def solve_case(case):
  [C, F, X] = [float(x) for x in stdin.readline().split()]
  answer = str(time_to_x(C, F, X))
  print "Case #%d: %s" % (case, answer)

def time_to_x(C, F, X):
  n_farms = 0
  time = X / 2
  while True:
    new_time = time - (X - C) / (n_farms * F + 2) + X / ((n_farms + 1) * F + 2)
    if new_time > time:
      return time
    n_farms += 1
    time = new_time

if __name__ == "__main__":
  main()

