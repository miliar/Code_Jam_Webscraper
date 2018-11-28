#!/usr/bin/python

# Solution to welcome problem
# Googld Code Jam, 2009 Qualification round
# Alex Roper <alexr@ugcs.caltech.edu>
# California Institute of Technology

# Basic approach: Move left to right, summing as we go. If you wanted the actual
# indices it would be a straightforward dynamic programming problem, as is it's
# even easier.

import sys

QUERY = "welcome to code jam"

def read_tokens(f):
  for line in f:
    yield line.strip()

def solve(query, omega):
  # Seed initially
  last = [0] * len(query)
  for i in range(len(query)):
    last[i] = omega.find(query[i], last[i - 1])
    if last[i] == -1: return 0

  # Now we attempt to increment it until we can't.
  total = 1
  inc = True
  while inc:
    inc = False
    for i in reversed(range(len(query))):
      if last[i] + 1 < len(omega): last[i] = omega.find(query[i], last[i] + 1)
      else: last[i] = -1
      if last[i] != -1:
        for j in range(i + 1, len(query)):
          lp = last[j - 1] if j > 0 else 0
          last[j] = omega.find(query[j], lp)
          if last[j] == -1:
            last[i] = -1
            break
      if last[i] != -1:
        inc = True
        total += 1
        break
# TOTOD
  return total

def main():
  # Read file
  rdr = read_tokens(open(sys.argv[1])).next
  N = int(rdr())
  for c in range(N):
    print "Case #%i: %s" % ((c + 1), str("%.4i" % solve(QUERY, rdr()))[-4:])

if __name__ == "__main__": main()
