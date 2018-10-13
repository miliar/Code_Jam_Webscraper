#!/usr/bin/python

def solve(a):
  n = len(a)
  m = len(a[0])
  i = 0
  sol = []
  for i in xrange(n):
    line = [' ' for j in xrange(m)]
    sol.append(line)

  for i in xrange(n):
    for  j in xrange(m):
      if a[i][j] == '.':
        sol[i][j] = '.'
      elif a[i][j] == '#' and sol[i][j] == ' ':
        if j == m - 1 or i == n - 1:
          return 0, []
        if a[i][j+1] != '#' or a[i+1][j] != '#' or \
            a[i+1][j+1] != '#':
          return 0, []
        sol[i][j], sol[i][j+1], sol[i+1][j], sol[i+1][j+1] = "/", "\\", "\\", "/"
  return 1, sol


def main():
  num_tests = int(raw_input())
  for test in xrange(num_tests):
    n, m = map(int, raw_input().split())
    a = []
    for i in xrange(n):
      a.append(raw_input())
    possible, sol = solve(a)
    print "Case #{0}:".format(test + 1)
    if not possible:
      print "Impossible"
    else:
      for i in xrange(n):
        print ''.join(sol[i])

main()
