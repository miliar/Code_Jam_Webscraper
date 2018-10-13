#!/usr/bin/python

import sys

fp = open(sys.argv[1],"r")
T = int(fp.readline())

for i in range(T): # for all cases
  pos_O = 1
  pos_B = 1 # robots begin at 1
  a = fp.readline().split()
  # first step
  last_robot = a[1]
  n = int(a[2]) # time waiting for last_robot to execute the command
  tot_n = n # amount of steps where the other robot can walk/press
  if last_robot == "O":
    pos_O = int(a[2])
  else:
    pos_B = int(a[2])
#  print "first move costs "+ str(n)
  if int(a[0]) == 1:
    print "Case #"+str(i+1)+": "+str(n) # was just one step to do
    continue
  for j in range(2,int(a[0])+1): # for all other steps
    if a[2*j-1] == last_robot: # same robot moves
      if last_robot == "O":
        last_pos = pos_O
        pos_O = int(a[2*j])
      else:
        last_pos = pos_B
        pos_B = int(a[2*j])
      n += (abs(int(a[2*j])-last_pos)+1) # it will take target - position+1 steps
#      print str(n)+" moves so far"
      tot_n += (abs(int(a[2*j])-last_pos)+1)
#      print "next move cost "+str(abs(int(a[2*j])-last_pos)+1)
    else: # other robot moves
      last_robot = a[2*j-1]
      if last_robot == "O":
        last_pos = pos_O
        pos_O = int(a[2*j])
      else:
        last_pos = pos_B
        pos_B = int(a[2*j])
      m = abs(int(a[2*j]) - last_pos)+1 # target - position +1 steps
#      print "robot "+a[2*j-1]+" needs "+str(m)+" moves, but had "+str(tot_n)+" time while the previous robot was working"
#      print "robot "+a[2*j-1]+" pressed button "+a[2*j]+" from pos "+str(last_pos)
      if m>tot_n: # this robot did not have enough time to finish his task
        n += m - tot_n # will take m-tot time to finish
        tot_n = m - tot_n # next robot has tot_n steps of free time
      else:
        n += 1
        tot_n = 1 # restart count on how much free time the other robot will have
#      print str(n)+" moves so far"
  print "Case #"+str(i+1)+": "+str(n)
