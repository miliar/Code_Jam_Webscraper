#!/usr/bin/env python

import sys
import numpy as np

T = int(raw_input())

for t in xrange(T):
  # solve the input
  Ac, Aj = raw_input().strip().split()
  Ac = int(Ac)
  Aj = int(Aj)
  
  activities = [] # start, end, duration, who
  ctotal = 0
  jtotal = 0

  C = np.zeros(Ac)
  D = np.zeros(Ac)
  for c in xrange(Ac):
    cc, dc = raw_input().strip().split()
    C[c] = int(cc)
    D[c] = int(dc)
    activities.append((C[c], D[c], D[c]-C[c], "C"))
    ctotal += D[c] - C[c]

  J = np.zeros(Aj)
  K = np.zeros(Aj)
  for j in xrange(Aj):
    jj, kj = raw_input().strip().split()
    J[j] = int(jj)
    K[j] = int(kj)
    activities.append((J[j], K[j], K[j]-J[j], "J"))
    jtotal += K[j] - J[j]

  activities.sort()

  cremain = 720 - ctotal
  jremain = 720 - jtotal

  result = 0

  if Aj + Ac == 1:
    # only one activity, so only two changes
    print "Case #{0}: {1}".format(t+1, 2)
    continue

  # at least two activities, so at least two proper gaps, and first != last

  ### FIND ALL GAPS AND THEIR TYPES, FIRST AND LAST

  first = activities[0][3]
  last = activities[-1][3]
  gaps = []

  prev = activities[0]

  for i in xrange(1, len(activities)):
    curr = activities[i]
    gaps.append((prev[3] + curr[3], curr[0] - prev[1])) # type of gap, length of gap
    prev = curr

  # add the last gap
  gaps.append((last + first, (1440 - activities[-1][1]) + activities[0][0]))

  # sort the gaps, then deal with them separately
  gaps.sort()

  # start with CC gaps
  i = 0
  while i < len(gaps) and gaps[i][0] == 'CC':
    gap = gaps[i]
    if gap[1] <= cremain:
      # gap is filled in
      cremain -= gap[1]
    else:
      # cannot fill in the gap, so need 2 changes
      result += 2
    i += 1

  # deal with CJ and JC gaps
  while i < len(gaps) and (gaps[i][0] == 'CJ' or gaps[i][0] == 'JC'):
    result += 1
    i += 1

  # deal with JJ gaps
  while i < len(gaps) and gaps[i][0] == 'JJ':
    gap = gaps[i]
    if gap[1] <= jremain:
      # gap is filled in
      jremain -= gap[1]
    else:
      # cannot fill in the gap, so need 2 changes
      result += 2
    i += 1

  # this is hopefully all

  print "Case #{0}: {1}".format(t+1, result)

  
