#! /usr/bin/python

import sys

def check_dist(nb_vendor, vendor, min_dist):
  for i in xrange(nb_vendor):
    for j in xrange(i+1, nb_vendor):
      if (vendor[j] - vendor[i]) < min_dist:
        return 0

  return 1

def solve(nb_vendor, vendor, min_dist):

  time = 0

  while check_dist(nb_vendor, vendor, min_dist) == 0:
    # one stop is a half-meter
    time += 0.5

    move = []
    move.append(-0.5)

    for i in xrange(1, nb_vendor-1):
      diff = vendor[i] - vendor[i-1]
      if diff > min_dist:
        move.append(-0.5)
      elif diff == min_dist:
        move.append(move[i-1])
      else:
        move.append(0.5)

    move.append(0.5)

    for i in xrange(nb_vendor):
      vendor[i] += move[i]

#    print vendor

  return time
      
fd = open(sys.argv[1])
num_cases = int(fd.readline())

for i in range(0, num_cases):
  line = fd.readline().split(" ")
  nb_pts = int(line[0])
  min_dist = int(line[1])
  nb_vendor = 0
  vendor = []
  for n in xrange(nb_pts):
    line = fd.readline().split(" ")
    pos = int(line[0])
    num_vendor = int(line[1])
    nb_vendor += num_vendor
    for v in xrange(num_vendor):
      vendor.append(pos)

#  print vendor

  output = solve(nb_vendor, vendor, min_dist)
  print "Case #%d:" % (i+1), output

