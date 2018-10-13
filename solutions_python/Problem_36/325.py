#!/usr/bin/python

import sys

def parse(f):
  return f.readline().rstrip()

def solve(s):
  pat = 'welcome to code jam'

  P = len(pat)
  S = len(s)
  dp = [[0 for i in range(P)] for i in range(S)]

  dp[S-1][P-1] = 0 + (pat[P-1] == s[S-1])
  for si in range(1,S):
    dp[S-si-1][P-1] = dp[S-si][P-1] + (pat[P-1] == s[S-si-1])

  for pi in range(1, P):
    for si in range(1, S):
      dp[S-si-1][P-pi-1] += dp[S-si][P-pi-1]
      if pat[P-pi-1] == s[S-si-1]:
        dp[S-si-1][P-pi-1] += dp[S-si][P-pi]
      dp[S-si-1][P-pi-1] %= 1000

  # print '\n'.join(map(lambda row: ' '.join(map(str, row)), dp))
  return dp[0][0] % 1000

def main():
  f = sys.stdin
  n = int(f.readline())
  for i in range(n):
    o = parse(f)
    print 'Case #%d: %04d' % (i+1, solve(o))

if __name__ == '__main__':
  main()
