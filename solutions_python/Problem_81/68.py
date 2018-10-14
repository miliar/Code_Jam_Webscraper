#! /usr/bin/python

import sys

def solve(nb_team, schedule):
  # calculate WP
  WP = []
  for i in xrange(nb_team):
    nb_win = 0
    nb_lost = 0
    for r in schedule[i]:
      if r == "1":
        nb_win += 1
      elif r == "0":
        nb_lost += 1

    WP.append([nb_win, nb_win + nb_lost])

  OWP = []
  for i in xrange(nb_team):
    owp_tmp = 0
    opp = 0
    for t in xrange(nb_team):
      r = schedule[i][t]
      if r == "1":
        owp_tmp += 1.0 * WP[t][0] / (WP[t][1] - 1)
        opp += 1
      elif r == "0":
        owp_tmp += 1.0 * (WP[t][0] - 1) / (WP[t][1] - 1)
        opp += 1

    OWP.append(owp_tmp / opp)

  for i in xrange(nb_team):
    RPI  = 0.25 * WP[i][0] / WP[i][1]
    RPI += 0.50 * OWP[i]
    oowp = 0
    for t in xrange(nb_team):
      if schedule[i][t] != ".":
        oowp += OWP[t]
    RPI += 0.25 * oowp / WP[i][1]
    print RPI

  return 1
      
fd = open(sys.argv[1])
num_cases = int(fd.readline())

for i in range(0, num_cases):
  nb_team = int(fd.readline().split(" ")[0])
  schedule = []
  for t in xrange(nb_team):
    s = fd.readline().split()[0]
    schedule.append(s)

  print "Case #%d:" % (i+1)
  output = solve(nb_team, schedule)

