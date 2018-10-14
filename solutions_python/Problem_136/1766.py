#!/usr/bin/python

import sys
import copy 

input_file = open(sys.argv[1], "r")
cookies_per_sec = 2
flag = 0 # toss 1rst line
case = 0
times = []
for line in input_file:
  if flag == 1:
    token = line.split()
    run = 1
    C = float(token[0])
    F = float(token[1])
    X = float(token[2])
    computed_time = 0
    while ( run == 1 ):
      time = float(X/cookies_per_sec) + computed_time # time if just wait
      times.append(time)
      computed_time = computed_time + float(C/cookies_per_sec) # wait time for next farm
      cookies_per_sec = cookies_per_sec + F
      if ( time > min(times) ):
        run = 0
      else:
        times.append(time)
    case = case + 1
    print ("Case #{0}: {1:.7f}".format(case,min(times)))
    times[:] = []
    cookies_per_sec = 2
  flag = 1
