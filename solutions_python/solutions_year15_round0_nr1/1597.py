#!/usr/bin/python
import sys, math

    

T = int(sys.stdin.readline())
for t in range(T):
  c, s = sys.stdin.readline().split(" ")
  shyness = map(int, s.strip())
  #print(shyness)
  #print c
  audience = 0
  n_invite = 0
  for i, v in enumerate(shyness):
      if audience < i:
          diff = i - audience
          n_invite += diff
          audience += diff
      audience += v
      #print i, v, n_invite
  print "Case #%d: %d" % ((t + 1), n_invite)
