#!/usr/bin/env python

import sys

DEBUG = False

def process(n, k):
  if (DEBUG): print 'Input: ' + str(n) + ' ' + str(k)

  # Initialize
  # snapper = [ [State?, Receiving power?] ]
  snapper = [[False, True]]
  for i in xrange(1, n):
    snapper.append([False, False])
  if (DEBUG): print 'List: ' + str(snapper)

  # Snaps
  for nsnap in xrange(1, k+1):
    if (DEBUG): print 'Snap ' + str(nsnap)

    # First snapper is always switching
    snapper[0][0] = not snapper[0][0]

    # State?
    for i in xrange(n-1, 0, -1):
      if (DEBUG): print 'State ' + str(i) + ': ' + str(snapper[i-1][1])
      if (snapper[i][1]):
        snapper[i][0] = not snapper[i][0]

    # Receiving power?
    for i in xrange(1, n):
      if (DEBUG): print 'Power ' + str(i) + ': ' + str(snapper[i-1][0]) + ', ' + str(snapper[i-1][1])
      if (snapper[i-1][0] and snapper[i-1][1]):
        snapper[i][1] = True
      else:
        snapper[i][1] = False
    
    # Debug
    if (DEBUG): print 'List: ' + str(snapper) + "\n"

  # Is the light enabled?
  if (snapper[n-1][0] and snapper[n-1][1]):
    return 'ON'
  else:
    return 'OFF'

ncases = int(sys.stdin.readline())
for ncase in xrange(1, ncases+1):
  if (DEBUG): print 'Case ' + str(ncase)
  line = sys.stdin.readline().strip("\n").split(" ")
  print 'Case #' + str(ncase) + ': ' + process(int(line[0]), int(line[1]))
  if (DEBUG): print "\n"
