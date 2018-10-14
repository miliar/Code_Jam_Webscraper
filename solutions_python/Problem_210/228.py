#!/usr/bin/env python3

import sys

def main():
  fi = sys.stdin
  fo = sys.stdout
  case_count = int(fi.readline().strip())
  for i in range(1, case_count+1):
    nc, nj, cs, js = read_input(fi)
    solution = solve(nc, nj, cs, js)
    display_and_clear(fo, i, solution)

def read_input(f):
  nc, nj = [int(arg) for arg in f.readline().split()]

  cs =[]
  for i in range(nc):
    b, e = [int(arg) for arg in f.readline().split()]
    cs.append((b, e, 0))

  js = []
  for i in range(nj):
    b, e = [int(arg) for arg in f.readline().split()]
    js.append((b, e, 1))

  return nc, nj, cs, js

def display_and_clear(f, i, solution):
  f.write('Case #%d: %s\n' % (i, solution))
  f.flush()

def solve(nc, nj, cs, js):
  if nc >= 2 or nj >= 2:
    cs = sorted(cs)
    js = sorted(js)

    if nc >= 2 and is_apart(cs) \
        or nj >= 2 and is_apart(js):
      return 4

  return 2

def is_apart(xs):
  return xs[1][1] - xs[0][0] > 720 \
    and xs[1][0] - xs[0][1] < 720

if __name__ == '__main__':
  main()

