#!/usr/bin/python

def solve(inp):
  inp = inp[1:].split(' ')
  s = int(inp[1])
  p = int(inp[2])
  scores = sorted([int(x) for x in inp[3:]], reverse=True)
  a = 0
  b = 0
  out = 0
  for score in scores:
    if score >= 3*p-2:
      a += 1
    elif score >= 3*p-4 and score >= p:
      b += 1
#  print '%d %d' % (a,b)
  return a + min(b, s)


import sys
input = sys.stdin.readlines()
input = input[1:]
for line, content in enumerate(input):
  print 'Case #%d: %d' % (line+1, solve(content))


