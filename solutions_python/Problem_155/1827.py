# -*- coding: utf-8 -*-

import sys

def solve(Smax, digits):
  if Smax == 0:
    return 0

  nstanding = int(digits[0])
  ans = 0
  for level in xrange(1, Smax+1):
    n = int(digits[level])
    if n == 0:
      continue
    if nstanding < level:
      added = level - nstanding
      ans += added
      nstanding += added
    nstanding += n 
  return ans

def main():

  T = int(sys.stdin.readline().rstrip("\n"))

  for t in xrange(1, T+1):
    param = sys.stdin.readline().rstrip("\n").split()
    Smax = int(param[0])
    digits = param[1]

    ans = solve(Smax, digits)

    print "Case #%d: %d"%(t, ans)

if __name__ == "__main__":
  main()
