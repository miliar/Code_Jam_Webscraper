#!/usr/bin/env python

T = int(raw_input())
for case in range(T):
  val = raw_input().split(' ')
  N = int(val[0])
  current = [1,1] # current pos
  wait = [0,0] # waiting time
  total = 0 # total time
  for i in range(N):
    color = val[2*i+1]
    bot = 0 if color == 'B' else 1
    dest = int(val[2*i+2])
    # time to move from current pos to dest
    time = abs(dest-current[bot]) - wait[bot]
    # and press the button
    time = time + 1 if time >= 0 else 1
    # update
    wait[bot] = 0
    wait[1-bot] = wait[1-bot] + time
    current[bot] = dest
    total = total + time
  print 'Case #%i: %i' % (case+1, total)
