#!/usr/bin/env python

import fileinput

def calculate(actions):
  # actions is a list of tuples: (time, is_departure, is_at_A)
  actions.sort()  # tuple is designed to sort correctly here
  # times don't matter, apart from ordering
  counts = {True: 0, False: 0}
  available = {True: 0, False: 0}
  for time, is_d, is_A in actions:
    if is_d:
      if available[is_A]:
        available[is_A] -= 1
      else:
        counts[is_A] += 1  # we didn't have enough trains here, add one
    else:
      available[is_A] += 1
  return counts[True], counts[False]

def to_minute_tuple(text):
  h, m = map(int, text.split(':'))
  return h * 60 + m

def read_actions(f, NA, NB, t):
  actions = []
  for i in range(NA + NB):
    depart, arrive = map(to_minute_tuple, f.readline().split())
    actions.append((depart, True, i < NA))
    actions.append((arrive + t, False, i >= NA))
  return actions

f = fileinput.input()
for i in range(1, 1 + int(f.readline())):
  turnaround_time = int(f.readline())
  NA, NB = map(int, f.readline().split())
  actions = read_actions(f, NA, NB, turnaround_time)
  print "Case #%d: %d %d" % ((i,) + calculate(actions))
