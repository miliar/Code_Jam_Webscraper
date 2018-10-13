# -*- coding: utf-8 -*-

from sys import stdin

debug = False
#debug = True

# given params as list of strings, return solution in string
def solve(params):
  solution = ""

  s = list(params[0])
  k = int(params[1])
  flips = 0

  for i in range(len(s)-k+1):
    if debug == True:
      print "i : " + str(i)
      print ''.join(s)
    if s[i] == '-':
      flips = flips + 1
      for j in range(i,i+k):
        if s[j] == '-':
          s[j] = '+'
        elif s[j] == '+':
          s[j] = '-'

  for i in range(len(s)-k,len(s)):
    if s[i] == '-':
      solution = "IMPOSSIBLE"

  if solution != "IMPOSSIBLE":
    solution = str(flips)

  return solution

# main
if __name__ == "__main__":
  # get number of cases
  nc = int(stdin.readline())

  # solve each test case
  for tc in range(1,nc+1):
    # read parameters for the test case
    params = stdin.readline().split()

    # print solution for current test case
    print "Case #" + str(tc) + ": " + solve(params)

