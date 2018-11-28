#! /usr/bin/python

import sys

def solve(n, a):
  bot = {}
  bot['O'] = 0
  bot['B'] = 0
  time = 0

  for i in range(n):
    if bot[a[i][0]] == a[i][1]:
      delta_time = 1
    else:
      delta_time = abs(bot[a[i][0]] - a[i][1]) + 1
      bot[a[i][0]] = a[i][1]

    time += delta_time

    for j in range(i+1, n):
      if a[j][0] != a[i][0]:
        diff = abs(bot[a[j][0]] - a[j][1])
        if diff <= delta_time:
          bot[a[j][0]] = a[j][1]
        elif bot[a[j][0]] > a[j][1]:
          bot[a[j][0]] -= delta_time
        else:
          bot[a[j][0]] += delta_time
        break

  return time - 1
      
fd = open(sys.argv[1])

num_cases = int(fd.readline())

for i in range(0, num_cases):
  a = fd.readline().split(" ")
  n = int(a[0])
  actions = []
  for j in range(n):
    actions.append([a[2*j+1], int(a[2*j+2])])
#  print actions
  output = solve(n, actions)
  print "Case #%d:" % (i+1), output

