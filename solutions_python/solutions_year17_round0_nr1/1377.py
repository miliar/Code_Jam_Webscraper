#!/usr/bin/python

HAPPY = '+'
SAD = '-'
SOLVED = True
UNSOLVED = False
IMPOSSIBLE = "IMPOSSIBLE"

def checkPattern(pattern):
  if any(SAD in s for s in pattern):
    return UNSOLVED
  else:
    return SOLVED

def flipCakes(pattern, start, end):
  for i in xrange(start, end):
    if (pattern[i] == HAPPY):
      pattern[i] = SAD
    else:
      pattern[i] = HAPPY
  return pattern

def happify(pattern, n):
  count = 0
  for i in xrange(0, len(pattern) - n + 1):
    if (pattern[i] == HAPPY):
      continue
    pattern = flipCakes(pattern, i, i + n)
    count = count + 1
    #print "DEBUG: ({}) {}".format(count, pattern)

  if (checkPattern(pattern) == SOLVED):
    return str(count)
  else:
    return IMPOSSIBLE

def main():
  # read a line with a single integer
  t = int(raw_input())
  for i in xrange(1, t + 1):
    # read a list of integers, 1 in this case
    pattern, length = [s for s in raw_input().split(" ")]
    n = int(length)
    answer = happify(list(pattern), n)
    ##print "DEBUG: s=[{}], ss=[{}]".format(s, answer)
    print "Case #{}: {}".format(i, answer)

main()
