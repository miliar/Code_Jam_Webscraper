# -*- coding: utf-8 -*-

from sys import stdin

debug = False
#debug = True

# given params as list of strings, return solution in string
def solve(params):
  solution = ""

  k = int(params[0])

  for i in range(len(str(k))):
    if debug == True:
      print("------------------------------------")
      print("i : " + str(i))
      print("k : " + str(k))
    if i > 0:
      # kd : current digit from right
      kd = k % (10 ** (i+1)) / (10 ** i)
      # kdp : (current - 1)th digit from right
      kdp = k % (10 ** (i)) / (10 ** (i-1))

      if kd > kdp:
        if debug == True:
          print("subtract : " + str((k % (10 ** i) + 1)))
        k = k - (k % (10 ** i) + 1)

  solution = str(k)

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

