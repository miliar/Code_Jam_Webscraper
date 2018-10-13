#!/usr/bin/env python

def tidify(N):
  answer = int(N)
  lower_pos = 1
  while (lower_pos < len(N)) and (int(N[lower_pos-1]) <= int(N[lower_pos])):
    lower_pos += 1

  if (lower_pos < len(N)):
    answer = tidify(str(int(N[0:lower_pos])-1) + "9"*(len(N)-lower_pos))

  return answer

def solve(case_nr):
  N = raw_input()
  answer = tidify(N)
  print "Case #%d: %d" % (case_nr, answer)


T = int(raw_input())

for i in xrange(T):
  solve(i+1)
