#!/usr/bin/env python

t = input()

for test in range(t):
  line = raw_input().strip().split(' ')
  n = int(line[0])
  last_time = 0
  time = 0
  poz = {'O': 1, 'B': 1}
  stopped_at = {'O': 0, 'B': 0}
  pushes = {'O': False, 'B': False}

  for i in range(n):
    who, dest = line[2*i+1], int(line[2*i+2])
    other = (who == 'O') and 'B' or 'O'
    # advance time to after he pushes the button
    if stopped_at[who] > time:
      time = stopped_at[who]
    # has the other one finished its job?
    if stopped_at[other] > time:
      time = stopped_at[other]
    # what time will he be available again?
    stopped_at[who] = max(stopped_at[who] + abs(poz[who] - dest) + 1, time + 1)
    poz[who] = dest
    last_time = max(last_time, stopped_at[who])

  print 'Case #{0}: {1}'.format(test+1, last_time)
