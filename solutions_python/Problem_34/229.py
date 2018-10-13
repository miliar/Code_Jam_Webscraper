#!/usr/bin/python

# Solution to alien problem
# Googld Code Jam, 2009 Qualification round
# Alex Roper <alexr@ugcs.caltech.edu>
# California Institute of Technology

import sys, re

def read_tokens(f):
  for line in f:
    for t in line.split():
      yield t

def trans_regex(word):
  """Turn a gcj regex into a re one."""
  rex = re.compile("(\([^)]*\))")
  out = ""
  tokens = rex.split(word)
  for t in filter(None, tokens):
    if t[0] == '(': out += "[%s]" % '|'.join(list(t[1:-1]))
    else: out += t
  return re.compile(out)

def main():
  # Read specs
  # L is word length
  # D is dict size
  # N is number of cases, as always.
  rdr = read_tokens(open(sys.argv[1])).next
  L, D, N = [int(rdr()) for _ in range(3)]

  # Read dictionary
  words = [rdr() for _ in range(D)]

  # Solve the test cases
  for c in range(N):
    # Turn pattern into a regular expression.
    rex = trans_regex(rdr())

    # Count the matches
    print "Case #%i: %i" % (c + 1, len(filter(None, map(rex.match, words))))

if __name__ == "__main__": main()
