#!/usr/bin/env python

file = open('euros.txt')
file = open('/home/ryan/Desktop/C-small-attempt0.in')
n = int(file.readline())

for i in range(n):
  
  line = file.readline()
  R = int(line.split(' ')[0])
  k = int(line.split(' ')[1])
  n = int(line.split(' ')[2])
  groups = file.readline()
  groups = groups.split(' ')
  groups = [int(group) for group in groups]
  euros = 0

  for t in range(R):
    num_people = 0
    to_append = []
    for group in groups:
      if num_people + group <=k:
        num_people += group
        to_append.append(group)
        groups = groups[1:]
      else:
        break
    groups += to_append
    euros += num_people

  print "Case #%s: %s" % (i+1, euros)
        
        
  
