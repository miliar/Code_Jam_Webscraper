#!/usr/bin/python

def solve(l, h, v):
  for i in xrange(l, h + 1):
    ok = True
    for x in v:
      if x % i != 0 and  i % x != 0:
        ok = False
        break
    if ok:
      return i
  return -1

def main():
  num_tests = int(raw_input())
  for test in xrange(num_tests):
    n, l, h = map(int, raw_input().split())
    v = map(int, raw_input().split())
    sol = solve(l, h, v)
    if sol == -1:
      print "Case #{0}: {1}".format(test+1, "NO")
    else:
      print "Case #{0}: {1}".format(test + 1 , sol)
main()
