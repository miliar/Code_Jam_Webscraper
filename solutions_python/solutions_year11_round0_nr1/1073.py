#!/usr/bin/python

import sys

f = open(sys.argv[1])

case = 0
for line in f:
  if case == 0:
    case += 1
    continue

  tokens = line.split()
  #print tokens

  steps = []

  loc = {'O':1, 'B':1}
  for i in range(1, len(tokens), 2):
    color = tokens[i]
    newpos = int(tokens[i+1])
    steps.append(color)
    steps.append(abs(newpos-loc[color]))
    loc[color] = newpos

  #print steps

  int_steps = 0
  tot_steps = 0
  prevcolor = None

  for i in range(0, len(steps), 2):
    color = steps[i]
    s = steps[i+1]

    if color != prevcolor:
      add_steps = s - int_steps
      if add_steps < 0:
        add_steps = 0

      tot_steps += add_steps + 1
      int_steps = add_steps + 1
      prevcolor = color

    elif color == prevcolor:
      tot_steps += s + 1
      int_steps += s + 1

  print "Case #%d: %d" % (case, tot_steps)
  case += 1



