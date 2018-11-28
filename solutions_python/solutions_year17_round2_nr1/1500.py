#!/usr/bin/python

import sys

f = open(sys.argv[1],'r')
t = int(f.readline())

for case in range(t):
  [d,n] = [int(i) for i in f.readline().split()]
  stats = [[0,0,0.0] for i in range(n)]
  for horse in range(n):
    [k,s] = [int(i) for i in f.readline().split()]
    stats[horse][0] = k
    stats[horse][1] = s
  stats.sort(key =lambda horse: horse[2])
  # calculate closest horse's time
  stats[0][2] = (d-stats[0][0])/stats[0][1]
  slowest = stats[0][2]
  slowestHorse = 0
  for horse in range(1,n):
    currentTime = (d-stats[horse][0])/stats[horse][1]
    if(currentTime < slowest):
      stats[horse][2] = slowest
    else:
      slowest = currentTime
      stats[horse][2] = currentTime
      slowestHorse = horse
  minSpeed = d/slowest

  # print(stats)

  print ("Case #" + str(case+1) + ": " + str(minSpeed))