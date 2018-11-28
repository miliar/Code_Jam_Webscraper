#!/usr/bin/python
import sys
f = open(sys.argv[1],'r')
out = open(sys.argv[2], 'w')
t= int(f.readline())
for i in range(0,t):
  temp = f.readline().split()
  smax = int(temp[0])
  people = temp[1]
  stand = int(people[0])
  friend = 0
  print "i=", i, "smax=", smax, "people=,",people
  for j in range(1,smax+1):
    while stand<j:
      friend += 1
      stand += 1
    stand += int(people[j])
  print friend,stand
  line = "Case #%s: %s\n" %(i+1,friend)
  out.write(line)
    
    
    

